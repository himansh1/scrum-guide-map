from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'shell.html').read_text().replace('__CSS__',(P/'style.css').read_text()).replace('__DATA__',(P/'data.json').read_text().replace('</','<\\/')).replace('__JS__',(P/'app.js').read_text())
(P/'index.html').write_text(s)
print(f'Built index.html: {len(s.encode()):,} bytes')
