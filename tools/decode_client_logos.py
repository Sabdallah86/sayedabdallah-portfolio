from pathlib import Path
import base64, json

src = Path('assets/client-logos-src/logos.json')
out = Path('assets/client-logos')
out.mkdir(parents=True, exist_ok=True)
data = json.loads(src.read_text(encoding='utf-8'))
written = 0
for slug, b64 in data.items():
    try:
        raw = base64.b64decode(b64)
        if raw:
            (out / f'{slug}.png').write_bytes(raw)
            written += 1
    except Exception as exc:
        print(f'Skipped {slug}: {exc}')
print(f'Decoded {written} client logos from merged logo data.')
