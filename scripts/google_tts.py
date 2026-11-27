"""Explicit opt-in Gemini TTS via documented REST Interactions API. Stdlib only."""
import argparse
import base64
import binascii
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request
import wave

from provider_config import api_key, setting

ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta/interactions'
DEFAULT_MODEL = 'gemini-3.8-flash-tts'


def payload(text: str, voice: str, style: str, model: str) -> dict:
    if not text.strip():
        raise ValueError('Skrip suara kosong. Isi teks yang hendak dibaca dahulu.')
    part = {'type': 'text', 'text': text}
    if style.strip():
        part['annotations'] = [{'type': 'speech_metadata', 'style': style}]
    return {
        'model': model,
        'input': [{'type': 'user_input', 'content': [part]}],
        'response_format': {'type': 'audio'},
        'generation_config': {'speech_config': [{'voice': voice}]},
    }


def audio_block(response: dict) -> tuple[bytes, str]:
    blocks = [c for step in response.get('steps', []) for c in step.get('content', []) if c.get('type') == 'audio' and c.get('data')]
    if not blocks:
        raise ValueError('Google tidak memulangkan audio. Semak model/kuota dan respons melalui dashboard; tiada retry automatik.')
    block = blocks[-1]
    try:
        return base64.b64decode(block['data'], validate=True), block.get('mime_type', block.get('mimeType', 'audio/wav'))
    except (binascii.Error, TypeError) as error:
        raise ValueError('Audio provider tidak sah; output tidak disimpan.') from error


def save_audio(data: bytes, mime: str, output: Path) -> None:
    # Preserve WAV bytes from the documented endpoint; wrap only explicitly typed PCM.
    if not data:
        raise ValueError('Audio kosong; output tidak disimpan.')
    if not (data[:4] == b'RIFF' and data[8:12] == b'WAVE'):
        if not mime.startswith('audio/pcm'):
            raise ValueError('Format audio tidak dijangka. Output WAV tidak disimpan.')
        rate = re.search(r'(?:rate|sample_rate)=(\d+)', mime)
        if not rate or not 8000 <= int(rate[1]) <= 192000 or len(data) % 2:
            raise ValueError('Metadata PCM tidak lengkap; jangan teka sample rate.')
        import io
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(int(rate[1]))
            wav.writeframes(data)
        data = buffer.getvalue()
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation also protects against races after preflight.
    with output.open('xb') as handle:
        handle.write(data)


def main() -> None:
    parser = argparse.ArgumentParser(description='Sediakan atau jana narasi Google TTS. Default: semakan tempatan sahaja.')
    parser.add_argument('--text-file', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--voice', default=setting('GEMINI_TTS_VOICE', 'Kore'))
    parser.add_argument('--model', default=setting('GEMINI_TTS_MODEL', DEFAULT_MODEL))
    parser.add_argument('--style', default='Bahasa Melayu Malaysia yang natural, jelas dan tenang.')
    parser.add_argument('--generate', action='store_true', help='Hantar skrip ke Google; mungkin menggunakan kuota/bayaran.')
    args = parser.parse_args()
    text = args.text_file.read_text(encoding='utf-8-sig').strip()
    body = payload(text, args.voice, args.style, args.model)
    if args.out.suffix.lower() != '.wav':
        raise ValueError('Gunakan output .wav untuk client ini.')
    if args.out.exists():
        raise ValueError('Output sudah wujud. Pilih nama baharu; fail asal tidak ditimpa.')
    print(f'Model: {args.model}; suara: {args.voice}; skrip: {len(text)} aksara; output: {args.out}')
    if not args.generate:
        print('Semakan tempatan sahaja. Tiada key diperlukan, API dipanggil atau audio dijana. Tambah --generate hanya selepas pengguna mengizinkan penjanaan.')
        return
    key = api_key('google')
    request = urllib.request.Request(ENDPOINT, data=json.dumps(body).encode('utf-8'), headers={'x-goog-api-key': key, 'Content-Type': 'application/json', 'User-Agent': 'MOTIVO/0.2'}, method='POST')
    with urllib.request.urlopen(request, timeout=180) as response:
        data, mime = audio_block(json.load(response))
    save_audio(data, mime, args.out)
    print(f'Audio disimpan: {args.out}. Dengar dan semak sebutan sebelum menyelaraskan sarikata.')


if __name__ == '__main__':
    try:
        main()
    except urllib.error.HTTPError as error:
        print(f'Google HTTP {error.code}. 400/404: semak model/voice; 401/403: semak key/projek; 429: semak kuota. Tiada retry automatik.', file=sys.stderr)
        sys.exit(1)
    except (ValueError, OSError, KeyError) as error:
        print(str(error) if isinstance(error, ValueError) and not isinstance(error, json.JSONDecodeError) else 'Gagal membaca/menyimpan audio atau menghubungi Google. Key tidak dipaparkan.', file=sys.stderr)
        sys.exit(1)
