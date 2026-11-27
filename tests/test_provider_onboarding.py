"""Test secret persistence and non-generating paths without provider access."""
import base64
import contextlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import wave

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import provider_config as config
import providers
import google_tts as tts


class LocalKeys(unittest.TestCase):
    def test_key_update_preserves_other_provider_and_comments(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '.env').write_text('# keep me\nNEXABOT_API_KEY=nxb_original\nGEMINI_API_KEY=old\nGEMINI_API_KEY=duplicate\nGEMINI_TTS_VOICE=Kore\n', encoding='utf-8-sig')
            config.save_key('google', 'test-local-key', root)
            result = (root / '.env').read_text()
            self.assertIn('# keep me', result)
            self.assertIn('NEXABOT_API_KEY=nxb_original', result)
            self.assertIn('GEMINI_TTS_VOICE=Kore', result)
            self.assertEqual(result.count('GEMINI_API_KEY='), 1)
            self.assertEqual(config.read_env(root)['GEMINI_API_KEY'], 'test-local-key')
            self.assertFalse((root / '.env.tmp').exists())

    def test_new_file_uses_template_without_overwriting_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template = '# optional\nNEXABOT_API_KEY=\nGEMINI_API_KEY=\n'
            (root / '.env.example').write_text(template)
            config.save_key('nexabot', 'nxb_local-test', root)
            self.assertEqual((root / '.env.example').read_text(), template)
            self.assertEqual(config.read_env(root)['NEXABOT_API_KEY'], 'nxb_local-test')

    def test_environment_precedence_and_empty_environment_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '.env').write_text('GEMINI_API_KEY="file-key"\n')
            with patch.dict(os.environ, {'GEMINI_API_KEY': 'env-key'}, clear=True):
                self.assertEqual(config.api_key('google', root), 'env-key')
            with patch.dict(os.environ, {'GEMINI_API_KEY': ''}, clear=True):
                self.assertEqual(config.api_key('google', root), 'file-key')

    def test_reject_multiline_and_placeholder_without_changing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '.env').write_text('NEXABOT_API_KEY=old\n')
            for value in ('', 'nxb_LETAK_KEY', 'first\nGEMINI_API_KEY=other', 'your_actual_key'):
                with self.assertRaises(ValueError):
                    config.save_key('nexabot', value, root)
            self.assertEqual((root / '.env').read_text(), 'NEXABOT_API_KEY=old\n')

    def test_status_never_prints_key(self):
        out = io.StringIO()
        with patch.object(providers, 'setting', return_value='private-test-secret'), contextlib.redirect_stdout(out):
            providers.status()
        self.assertNotIn('private-test-secret', out.getvalue())

    def test_noninteractive_connect_refuses_echo_fallback(self):
        with patch.object(sys, 'argv', ['providers.py', 'connect', 'google']), patch.object(sys.stdin, 'isatty', return_value=False), patch.object(providers.getpass, 'getpass') as prompt, contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(ValueError):
                providers.main()
            prompt.assert_not_called()


class GoogleNarration(unittest.TestCase):
    def test_script_preserved_and_direction_not_spoken_text(self):
        text = 'Selamat datang. Ini skrip sebenar.'
        result = tts.payload(text, 'Kore', 'tenang', 'test-model')
        self.assertEqual(result['input'][0]['content'][0]['text'], text)
        self.assertNotIn('tenang', result['input'][0]['content'][0]['text'])
        self.assertEqual(result['response_format'], {'type': 'audio'})

    def test_dry_run_does_not_read_key_call_api_or_write_audio(self):
        with tempfile.TemporaryDirectory() as tmp:
            text, out = Path(tmp) / 'voice.txt', Path(tmp) / 'voice.wav'
            text.write_text('Selamat datang.', encoding='utf-8')
            with patch.object(sys, 'argv', ['google_tts.py', '--text-file', str(text), '--out', str(out)]), patch.object(tts, 'api_key') as key, patch.object(tts.urllib.request, 'urlopen') as network, contextlib.redirect_stdout(io.StringIO()):
                tts.main()
                key.assert_not_called()
                network.assert_not_called()
                self.assertFalse(out.exists())

    def test_existing_output_stops_before_paid_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            text, out = Path(tmp) / 'voice.txt', Path(tmp) / 'voice.wav'
            text.write_text('Selamat datang.')
            out.write_bytes(b'original')
            with patch.object(sys, 'argv', ['google_tts.py', '--text-file', str(text), '--out', str(out), '--generate']), patch.object(tts.urllib.request, 'urlopen') as network:
                with self.assertRaises(ValueError):
                    tts.main()
                network.assert_not_called()
            self.assertEqual(out.read_bytes(), b'original')

    def test_audio_response_and_pcm_have_valid_wav_metadata(self):
        pcm = b'\x00\x00' * 240
        response = {'steps': [{'content': [{'type': 'audio', 'data': base64.b64encode(pcm).decode(), 'mime_type': 'audio/pcm;rate=24000'}]}]}
        data, mime = tts.audio_block(response)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'voice.wav'
            tts.save_audio(data, mime, out)
            with wave.open(str(out), 'rb') as wav:
                self.assertEqual((wav.getnchannels(), wav.getframerate(), wav.getnframes()), (1, 24000, 240))
                self.assertEqual(wav.readframes(240), pcm)

    def test_missing_audio_and_unknown_format_rejected(self):
        with self.assertRaises(ValueError):
            tts.audio_block({'steps': []})
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'voice.wav'
            with self.assertRaises(ValueError):
                tts.save_audio(b'not a wav', 'audio/mpeg', out)
            with self.assertRaises(ValueError):
                tts.save_audio(b'\x00\x00', 'audio/pcm', out)
            self.assertFalse(out.exists())

    def test_opt_in_sends_only_google_key_in_header_not_body_or_url(self):
        audio = io.BytesIO()
        with wave.open(audio, 'wb') as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(24000)
            wav.writeframes(b'\x00\x00' * 240)
        response = {'steps': [{'content': [{'type': 'audio', 'data': base64.b64encode(audio.getvalue()).decode()}]}]}
        with tempfile.TemporaryDirectory() as tmp:
            text, out = Path(tmp) / 'voice.txt', Path(tmp) / 'voice.wav'
            text.write_text('Selamat datang.')
            with patch.object(sys, 'argv', ['google_tts.py', '--text-file', str(text), '--out', str(out), '--generate']), patch.object(tts, 'api_key', return_value='private-test-key'), patch.object(tts.urllib.request, 'urlopen') as network, contextlib.redirect_stdout(io.StringIO()) as stdout:
                network.return_value.__enter__.return_value = io.BytesIO(json.dumps(response).encode())
                tts.main()
                req = network.call_args.args[0]
                self.assertEqual(req.get_header('X-goog-api-key'), 'private-test-key')
                self.assertNotIn('private-test-key', req.full_url)
                self.assertNotIn('private-test-key', req.data.decode())
                self.assertNotIn('private-test-key', stdout.getvalue())
            self.assertEqual(out.read_bytes(), audio.getvalue())


if __name__ == '__main__':
    unittest.main()
