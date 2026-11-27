"""Small local .env reader/writer. No network calls or credential logging."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYS = {'nexabot': 'NEXABOT_API_KEY', 'google': 'GEMINI_API_KEY'}


def read_env(root: Path = ROOT) -> dict[str, str]:
    result = {}
    path = root / '.env'
    if path.exists():
        for raw in path.read_text(encoding='utf-8-sig').splitlines():
            line = raw.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            name, value = line.split('=', 1)
            result[name.strip()] = value.strip().strip('\"\'')
    return result


def setting(name: str, default: str = '', root: Path = ROOT) -> str:
    return os.environ.get(name, '').strip() or read_env(root).get(name, '').strip() or default


def usable_key(key: str) -> bool:
    return bool(key) and not any(x in key.lower() for x in (
        'letak', 'gantikan', 'your_key', 'your_actual_key', 'xxxxxxxx', 'paste_here',
    ))


def api_key(provider: str, root: Path = ROOT) -> str:
    name = KEYS[provider]
    key = setting(name, root=root)
    if not usable_key(key):
        raise ValueError(f'{name} belum diset. Jalankan npm run connect -- {provider}, atau isi baris itu dalam .env.')
    return key


def save_key(provider: str, key: str, root: Path = ROOT) -> None:
    if not usable_key(key) or any(c.isspace() for c in key) or any(c in key for c in '\"\''):
        raise ValueError('Key kosong/contoh atau format tidak sah. Tampal key sahaja tanpa tanda petik.')
    name = KEYS[provider]
    path = root / '.env'
    template = root / '.env.example'
    old = path.read_text(encoding='utf-8-sig') if path.exists() else (template.read_text(encoding='utf-8-sig') if template.exists() else '')
    lines, replaced = [], False
    for line in old.splitlines():
        if line.strip().split('=', 1)[0].strip() == name and '=' in line:
            if not replaced:
                lines.append(f'{name}={key}')
            replaced = True
        else:
            lines.append(line)
    if not replaced:
        lines.append(f'{name}={key}')
    temporary = root / '.env.tmp'
    try:
        with temporary.open('w', encoding='utf-8') as handle:
            if os.name != 'nt':
                os.chmod(temporary, 0o600)
            handle.write('\n'.join(lines) + '\n')
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)
