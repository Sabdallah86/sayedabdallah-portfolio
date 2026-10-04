"""Verify reviewed portfolio additions without rewriting runtime data."""
from pathlib import Path
import json

text = Path('script.js').read_text(encoding='utf-8')
start = text.index('const categoryData = ') + len('const categoryData = ')
end = text.index('function escapeHTML', start)
data = json.loads(text[start:end].strip().removesuffix(';'))
required = {
    'commercial': {'SYQvIrjg8qw'},
    'series': {'gLtyCZRuCCo'},
    'more-work': {'G1aMXgXTAog', 'fbrKZPloehw', 'T1VOBnWPwtE', '0UY-_mTpUDA', 'oIS4SghLtSs', 's72BulxLJgM', '5jaNOku5Tw0'},
}
for key, ids in required.items():
    actual = {p.get('youtube') for p in data[key]['projects']}
    if not ids.issubset(actual):
        raise RuntimeError(f'Missing reviewed portfolio videos in {key}: {ids - actual}')
for key, slug in [('sports', 'al-ahly-club'), ('events', 'ciff')]:
    if not data[key]['collections'][slug]['projects']:
        raise RuntimeError(f'Empty portfolio collection: {key}/{slug}')
print('Reviewed portfolio video additions are present.')
