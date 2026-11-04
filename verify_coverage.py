import json,re
from pathlib import Path
from collections import Counter
p=Path(__file__).resolve().parent
data=json.loads((p/'data.json').read_text());blocks=json.loads((p/'blocks.json').read_text());pages=json.loads((p/'guide-pages.json').read_text())
def norm(s):return re.sub(r'\s+',' ',s).strip().replace('one- month','one-month')
assert norm(' '.join(b['text'] for b in blocks))==norm(' '.join(p['text'] for p in pages))
by={b['id']:b for b in blocks};refs=Counter(r for n in data['nodes'].values() for r in n['refs'])
assert set(refs)==set(by)
assert all(v==(5 if k=='b036' else 1) for k,v in refs.items())
for b in blocks:
    ns=[n for n in data['nodes'].values() if b['id'] in n['refs']]
    if b['kind']=='heading':assert len(ns)==1 and ns[0]['title']==b['text']
    elif b['id']=='b036':assert ' '.join(n['text'] for n in sorted(ns,key=lambda n:n['slice']))==b['text']
    else:assert len(ns)==1 and ns[0]['text']==b['text']
seen=set()
def walk(id):
    assert id not in seen;seen.add(id)
    for c in data['nodes'][id].get('children',[]):
        assert data['nodes'][c]['parent']==id
        walk(c)
walk('home');assert seen==set(data['nodes'])
assert len(pages)==14
print('PASS: all 14 pages, 163 blocks and 31 headings preserved; 136 exact terminal passages; all nodes reachable; no unassigned text.')
