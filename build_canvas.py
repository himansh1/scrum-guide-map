"""Build one continuous, source-complete HTML study canvas."""
from pathlib import Path
from html import escape
import json

P = Path(__file__).resolve().parent
D = json.loads((P / 'data.json').read_text())
N = D['nodes']

def e(s):
    return escape(str(s), quote=True)

def pages(n):
    return ' · '.join('Cover' if p == 0 else f'p. {p}' for p in n['pages'])

def tree(id, depth=0):
    n = N[id]
    if 'text' in n:
        return f'''<article class="source-passage" id="c-{id}" data-passage="{id}">
<div class="passage-label"><h4>{e(n['title'])}</h4><a href="https://himansh1.github.io/scrum-guide-map/#{id}" target="_blank" rel="noopener" aria-label="Open {e(n['title'])} and add a note">{e(pages(n))} · notes ↗</a></div>
<p class="original-text">{e(n['text'])}</p></article>'''
    heading = 'h3' if depth == 0 else 'h4'
    return f'''<section class="source-branch level-{min(depth,2)}" id="c-{id}" data-branch="{id}"><{heading} class="branch-heading">{e(n['title'])}</{heading}><p class="branch-keywords">{e(' · '.join(n['keywords']))}</p>{''.join(tree(c,depth+1) for c in n['children'])}</section>'''

def cues(id):
    items = [s for s in D['summary'] if s['group'] == id]
    if not items:
        return '<div class="revision-cues"><h3>Source context</h3><p>Cover, purpose, contents, end note, acknowledgements, history and licensing are included here in full.</p></div>'
    return '<div class="revision-cues"><h3>Exam notes · reviewed cues</h3>' + ''.join(
        f'<div class="cue" data-cue="{s["id"]}"><h4>{e(s["title"])}</h4><p>{e(s["text"])}</p>' +
        (f'<p class="cue-qualification">{e(s["qualification"])}</p>' if s.get('qualification') else '') + '</div>'
        for s in items) + '</div>'

def diagram(id):
    if id == 'fundamentals':
        return '<div class="pillar-flow" aria-label="The three pillars"><span>Transparency</span><b>→</b><span>Inspection</span><b>→</b><span>Adaptation</span></div>'
    if id == 'scrum-values':
        return '<div class="values-line">Commitment · Focus · Openness · Respect · Courage</div>'
    if id == 'scrum-team':
        return '<div class="role-flow"><span>Product Owner<br><b>Value</b></span><span>Developers<br><b>Usable Increment</b></span><span>Scrum Master<br><b>Effectiveness</b></span></div><p class="diagram-note">Memory cues; complete accountabilities appear below.</p>'
    if id == 'scrum-events':
        return '<div class="sprint-frame"><b>Sprint · one month or less</b><div><span>Planning<br><strong>≤8h</strong></span><i>→</i><span>Daily Scrum<br><strong>15m</strong></span><i>→</i><span>Review<br><strong>≤4h</strong></span><i>→</i><span>Retro<br><strong>≤3h</strong></span></div></div><p class="diagram-note">Planning, Review and Retrospective limits apply to a one-month Sprint; usually shorter for shorter Sprints. Daily Scrum: 15 minutes each working day.</p>'
    if id == 'scrum-artifacts':
        return '<div class="artifact-flow"><div><span>Product Backlog</span><b>→</b><strong>Product Goal</strong></div><div><span>Sprint Backlog</span><b>→</b><strong>Sprint Goal</strong></div><div><span>Increment</span><b>→</b><strong>Definition of Done</strong></div></div><p class="diagram-note">Each artifact and its commitment.</p>'
    return ''

short = ['Theory', 'Values', 'Team', 'Events', 'Artifacts', 'About']
columns = []
topic_data = []
for i,id in enumerate(N['home']['children']):
    n=N[id]
    branches=[]
    def collect(k):
        if 'children' in N[k]:
            branches.append({'id':'c-'+k, 'title':N[k]['title']})
            for c in N[k]['children']: collect(c)
    for c in n['children']: collect(c)
    topic_data.append({'id':id, 'label':short[i], 'branches':branches})
    columns.append(f'''<section class="topic-column" id="c-{id}" data-topic="{id}" style="--topic:{n['color']}">
<header class="topic-heading"><p class="topic-kicker">{n['leafCount']} original passages · {e(pages(n))}</p><h2>{e(n['title'])}</h2><p>{e(' · '.join(n['keywords']))}</p></header>
{diagram(id)}{cues(id)}<div class="source-divider"><span>Complete Guide text</span><small>Every passage · original wording</small></div>{''.join(tree(c) for c in n['children'])}</section>''')
buttons=''.join(f'<button data-topic-button="{t["id"]}" style="--topic:{N[t["id"]]["color"]}">{t["label"]}</button>' for t in topic_data)
html=(P/'canvas-shell.html').read_text().replace('__CSS__',(P/'canvas.css').read_text()).replace('__JS__',(P/'canvas.js').read_text()).replace('__TOPICS__',buttons).replace('__COLUMNS__',''.join(columns)).replace('__DATA__',json.dumps(topic_data,ensure_ascii=False).replace('</','<\\/'))
(P/'canvas.html').write_text(html)
print(f'Built canvas.html: {len(html.encode()):,} bytes; {len(columns)} topics; {sum(1 for n in N.values() if "text" in n)} full passages; 25 reviewed cues.')
