"""Local credential handling only. Never calls the provider."""
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from nexabot_client import load_api_key


class Credentials(unittest.TestCase):
    def test_environment_overrides_file(self):
        with patch.dict(os.environ, {'NEXABOT_API_KEY': 'nxb_environment'}, clear=True), patch.object(Path, 'exists', return_value=True), patch.object(Path, 'read_text', return_value='NEXABOT_API_KEY=nxb_file'):
            self.assertEqual(load_api_key(), 'nxb_environment')

    def test_blank_file_does_not_send_empty_key(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(Path, 'exists', return_value=True), patch.object(Path, 'read_text', return_value='NEXABOT_API_KEY='):
            with self.assertRaises(RuntimeError):
                load_api_key()

    def test_placeholder_rejected(self):
        with patch.dict(os.environ, {'NEXABOT_API_KEY': 'nxb_LETAK_API_KEY_DI_SINI'}, clear=True), patch.object(Path, 'exists', return_value=False):
            with self.assertRaises(RuntimeError):
                load_api_key()

    def test_quoted_file_key(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(Path, 'exists', return_value=True), patch.object(Path, 'read_text', return_value='NEXABOT_API_KEY="nxb_file"'):
            self.assertEqual(load_api_key(), 'nxb_file')


if __name__ == '__main__':
    unittest.main()
