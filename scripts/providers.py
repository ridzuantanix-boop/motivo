"""Status, hidden local key entry and explicit read-only authentication checks."""
import argparse
import getpass
import json
import os
import sys
import urllib.error
import urllib.request

from provider_config import KEYS, api_key, save_key, setting, usable_key

LINKS = {
    'nexabot': 'https://nexabot.id/api-keys',
    'google': 'https://aistudio.google.com/apikey',
}


def status() -> None:
    for provider, name in KEYS.items():
        label = 'key tersedia; belum disahkan' if usable_key(setting(name)) else 'belum disambung; pilihan sahaja'
        print(f'{provider}: {label}')
    print('Tanpa API: guna gambar, klip dan rakaman sendiri. TTS manual: https://aistudio.google.com/generate-speech')
    print('Seterusnya, cakap kepada agent: Bimbing aku buat video pertama dengan MOTIVO.')


def check(provider: str) -> None:
    key = api_key(provider)
    url = 'https://nexabot.id/api/v1/api/credit' if provider == 'nexabot' else 'https://generativelanguage.googleapis.com/v1beta/models'
    header = 'x-api-key' if provider == 'nexabot' else 'x-goog-api-key'
    request = urllib.request.Request(url, headers={header: key, 'User-Agent': 'MOTIVO/0.2'})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    if data.get('ok') is False or data.get('error'):
        raise ValueError('Provider menolak semakan. Semak key/akaun pada dashboard provider.')
    print(f'{provider}: semakan baca sahaja berjaya. Tiada media dijana. Kuota/model penjanaan masih bergantung pada akaun.')


def main() -> None:
    parser = argparse.ArgumentParser(description='MOTIVO sambungan provider. Tiada key dipaparkan.')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('status')
    for command in ('connect', 'check'):
        child = sub.add_parser(command)
        child.add_argument('provider', choices=KEYS)
    args = parser.parse_args()
    if args.command == 'status':
        status()
    elif args.command == 'check':
        check(args.provider)
    else:
        print(f'Dapatkan key sendiri: {LINKS[args.provider]}')
        if not sys.stdin.isatty():
            raise ValueError('Buka terminal interaktif sendiri untuk masukkan key secara tersembunyi. Atau isi .env dalam editor; jangan tampal key dalam chat/command.')
        key = getpass.getpass('Tampal API key (input disembunyikan): ').strip()
        save_key(args.provider, key)
        print('Key disimpan dalam .env tempatan. Tiada semakan API atau penjanaan dibuat.')
        if os.environ.get(KEYS[args.provider]):
            print('Nota: environment variable sedia ada mengambil keutamaan berbanding .env. Kosongkan/kemas kini variable itu jika mahu guna key baharu.')
        print(f'Untuk semakan baca sahaja: npm run provider:check -- {args.provider}')


if __name__ == '__main__':
    try:
        main()
    except urllib.error.HTTPError as error:
        messages = {401: 'Key ditolak. Salin key yang betul dari dashboard.', 403: 'Akses ditolak. Semak key, projek dan kebenaran provider.', 429: 'Had/kuota dicapai. Semak akaun; jangan ulang berkali-kali.'}
        print(f'HTTP {error.code}: {messages.get(error.code, "Provider belum dapat dihubungi. Cuba semula kemudian.")}', file=sys.stderr)
        sys.exit(1)
    except (ValueError, OSError, EOFError, json.JSONDecodeError) as error:
        # Network exceptions may contain URLs: do not print their raw text.
        print(str(error) if isinstance(error, ValueError) and not isinstance(error, json.JSONDecodeError) else 'Semakan gagal. Semak sambungan/provider atau fail .env.', file=sys.stderr)
        sys.exit(1)
