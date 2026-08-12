from pathlib import Path
import json

base_path = Path('assets/client-logos-src/logos.json')
extra_path = Path('assets/client-logos-src/logos-missing.json')
base = json.loads(base_path.read_text(encoding='utf-8'))
extra = json.loads(extra_path.read_text(encoding='utf-8'))
base.update(extra)
base_path.write_text(json.dumps(base, separators=(',', ':')), encoding='utf-8')
print('Client logo data keys:', ', '.join(sorted(base)))
