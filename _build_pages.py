# Generates privacy/<app>/index.html from markdown. Run: python _build_pages.py   (optional - the HTML is already built)
import html, re, pathlib
HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} - SAMZLAB</title><meta name="robots" content="index,follow"><link rel="icon" href="../../assets/img/favicon.png">
<link rel="stylesheet" href="../../assets/css/style.css"></head><body>
<header class="nav"><div class="wrap"><a class="brand" href="../../">{mark}SAMZLAB</a><nav class="links"><a href="../../#apps">Apps</a><a href="../../#contact">Contact</a></nav></div></header>
<main class="wrap doc"><a class="back" href="../../">&larr; All apps</a>
'''
FOOT = '''<p class="meta" style="margin-top:36px">Questions about this policy: <a href="mailto:samzlabpk@gmail.com">samzlabpk@gmail.com</a></p></main>
<footer><div class="wrap"><span>&copy; <span id="year"></span> SAMZLAB</span></div></footer><script>document.getElementById("year").textContent=new Date().getFullYear()</script></body></html>'''
MARK = '<svg aria-hidden="true" viewBox="0 0 120 120"><defs><clipPath id="sl"><path d="M52 22V50L28 88Q24 96 34 96H86Q96 96 92 88L68 50V22Z"/></clipPath></defs><g clip-path="url(#sl)"><path d="M16 76Q38 62 60 76T104 76V110H16Z" fill="#FF8A63"/></g><path d="M46 22H74M52 22V50L28 88Q24 96 34 96H86Q96 96 92 88L68 50V22" fill="none" stroke="currentColor" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60" cy="62" r="3.4" fill="currentColor"/><circle cx="67" cy="49" r="2.4" fill="currentColor"/><circle cx="58" cy="38" r="2" fill="currentColor"/></svg>'
def inline(s):
    s = html.escape(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s
def md(text):
    out, para, items = [], [], []
    def flush():
        nonlocal para, items
        if para: out.append('<p>' + inline(' '.join(para)) + '</p>'); para = []
        if items: out.append('<ul>' + ''.join('<li>' + inline(i) + '</li>' for i in items) + '</ul>'); items = []
    for l in text.splitlines():
        if l.startswith('# '): flush(); out.append('<h1>' + inline(l[2:]) + '</h1>')
        elif l.startswith('## '): flush(); out.append('<h2>' + inline(l[3:]) + '</h2>')
        elif l.startswith('- '): 
            if para: flush()
            items.append(l[2:])
        elif not l.strip(): flush()
        elif l.startswith('Effective:') or l.startswith('_Last updated'): flush(); out.append('<p class="meta">' + inline(l.strip('_')) + '</p>')
        else:
            if items: flush()
            para.append(l.strip())
    flush(); return '\n'.join(out)
def link(s): return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
for kind, slug, title, src in (('privacy', 'rimota', 'Rimota Privacy Policy', 'policy_rimota.md'), ('privacy', 'languardpro', 'LanGuard Pro Privacy Policy', 'policy_languardpro.md')):
    body = link(md(pathlib.Path(src).read_text(encoding='utf-8')))
    pathlib.Path(f'{kind}/{slug}').mkdir(parents=True, exist_ok=True)
    pathlib.Path(f'{kind}/{slug}/index.html').write_text(HEAD.format(title=title, mark=MARK) + body + FOOT.replace('Questions about this policy', 'Questions'), encoding='utf-8')
print('built')
