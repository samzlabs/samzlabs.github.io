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
MARK = '<svg viewBox="0 0 120 120" aria-hidden="true"><path d="M61 37C77 36 88 49 87 64C86 80 74 90 59 89C44 88 34 76 35 62C36 47 46 38 62 37Z" fill="none" stroke="currentColor" stroke-width="10" stroke-linejoin="round"/><path d="M40 19C52 16 70 17 82 19" stroke="#FF8A63" stroke-width="9" stroke-linecap="round" fill="none"/><circle cx="61" cy="106" r="8" fill="#FF8A63"/></svg>'
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
for slug, title, src in (('rimota', 'Rimota Privacy Policy', 'policy_rimota.md'), ('languardpro', 'LanGuard Pro Privacy Policy', 'policy_languardpro.md')):
    body = md(pathlib.Path(src).read_text(encoding='utf-8'))
    pathlib.Path(f'privacy/{slug}/index.html').write_text(HEAD.format(title=title, mark=MARK) + body + FOOT, encoding='utf-8')
print('built')
