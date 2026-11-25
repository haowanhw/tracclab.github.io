"""Build the static TRACC Lab website using only the Python standard library."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content/site.json').read_text())


def e(value):
    return escape(str(value), quote=True)


def paragraphs(values):
    return ''.join(f'<p>{e(value)}</p>' for value in values)


def items(values):
    return '<ul>' + ''.join(f'<li>{e(value)}</li>' for value in values) + '</ul>'


def header(current):
    links = [('index.html', 'Home'), ('research.html', 'Research'), ('people.html', 'People'), ('news.html', 'News')]
    nav = ''.join(f'<a href="{url}"' + (' aria-current="page"' if url == current else '') + f'>{label}</a>' for url, label in links)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="institution-bar"><div class="container"><span>University of Rochester</span><span>Supportive Care in Cancer</span></div></div>
<header class="site-header"><div class="container header-inner">
  <a class="brand" href="index.html" aria-label="TRACC Lab home"><img src="assets/tracc-logo.png" width="2172" height="724" alt="TRACC Lab — Translating Research into Action in Cancer Care"></a>
  <nav id="site-nav" aria-label="Main navigation">{nav}<a class="nav-contact" href="index.html#contact">Contact</a></nav>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open navigation"><span></span><span></span></button>
</div></header>'''


def footer():
    return f'''<footer class="site-footer"><div class="container footer-grid">
  <div><p class="footer-name">TRACC Lab</p><p>{e(DATA['full_name'])}</p></div>
  <div><p>Supportive Care in Cancer<br>Department of Surgery<br>University of Rochester Medical Center</p></div>
  <div><p>Rochester, New York</p><a href="mailto:{e(DATA['email'])}">{e(DATA['email'])}</a><a class="footer-scholar" href="{e(DATA['scholar'])}" target="_blank" rel="noopener noreferrer">Google Scholar</a></div>
</div><div class="container footer-bottom"><span>TRACC Lab · University of Rochester</span><a href="index.html#contact">Contact the lab</a></div></footer>'''


def page(filename, title, description, body):
    html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b3157"><meta name="description" content="{e(description)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website">
<title>{e(title)}</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="styles.css"><script src="script.js" defer></script>
</head><body>{header(filename)}<main id="main">{body}</main>{footer()}</body></html>
'''
    (ROOT / filename).write_text(html)


def contact():
    return f'''<section class="contact-section" id="contact" aria-labelledby="contact-heading"><div class="container contact-inner">
<div><p class="eyebrow">Contact us</p><h2 id="contact-heading">Let’s translate evidence<br>into practice, together.</h2></div>
<div><p>Interested in our work, have a general question, or want to partner with the TRACC Lab?</p><p>For implementation research questions and collaboration opportunities, contact our principal investigator.</p><p class="contact-name">Junqiang Zhao, PhD</p><a class="email-link" href="mailto:{e(DATA['email'])}">{e(DATA['email'])}</a></div>
</div></section>'''


def home():
    expertise = ''.join(f'<article class="expertise-item"><h3>{e(x["title"])}</h3>{items(x["items"])}</article>' for x in DATA['expertise'])
    research = ''.join(f'<article class="research-preview"><h3><a href="research.html#{e(x["id"])}">{e(x["title"])}</a></h3><p>{e(x["short"])}</p><a class="text-link" href="research.html#{e(x["id"])}">Explore this research area</a></article>' for x in DATA['areas'])
    n = DATA['news']
    return f'''<section class="container home-hero">
  <div class="hero-copy"><p class="eyebrow">TRACC Lab</p><h1>Translating research into action in <span>cancer care.</span></h1><p class="lead">{e(DATA['mission'])}</p><div class="hero-actions"><a class="button" href="research.html">Explore our research</a><a class="text-link" href="people.html">Meet the team</a></div></div>
</section>
<section class="expertise-section" id="expertise"><div class="container"><div class="section-heading"><p class="eyebrow">What we bring</p><h2>Research expertise</h2></div><div class="expertise-grid">{expertise}</div></div></section>
<section class="container section"><div class="section-heading heading-with-link"><div><p class="eyebrow">What we study</p><h2>Research areas</h2></div><a class="text-link" href="research.html">Research and current projects</a></div><div class="research-preview-grid">{research}</div></section>
<section class="news-band"><div class="container news-feature"><a class="news-image-link" href="news.html#surgery-symposium-2026" aria-label="Read about Yufei Jia’s symposium presentation"><img src="{e(n['photo'])}" width="503" height="670" alt="Yufei Jia presenting research at the Department of Surgery Scientific Symposium" loading="lazy"></a><div><p class="eyebrow">Lab news · {e(n['year'])}</p><h2><a href="news.html#surgery-symposium-2026">{e(n['title'])}</a></h2><a class="text-link" href="news.html#surgery-symposium-2026">Read the news</a></div></div></section>
{contact()}'''


def project_card(project):
    link = f'<a class="text-link" href="{e(project["link"])}" target="_blank" rel="noopener noreferrer">Read the project publication</a>' if project.get('link') else ''
    return f'''<article class="project" id="{e(project['id'])}"><p class="project-label">Current project</p><h3>{e(project['title'])}</h3><p>{e(project['summary'])}</p><p class="project-methods">{e(project['methods'])}<span aria-hidden="true"> · </span>{e(project['framework'])}</p><details><summary>Project overview and methods</summary><div class="details-body">{paragraphs(project['paragraphs'])}{link}</div></details></article>'''


def research():
    sidebar = ''.join(f'<a href="#{e(x["id"])}">{e(x["title"])}</a>' for x in DATA['areas'])
    sections = []
    for area in DATA['areas']:
        focus = items(area.get('focus', [])) if area.get('focus') else ''
        projects = ''.join(project_card(p) for p in DATA['projects'] if p['area'] == area['id'])
        supportive = ''
        if area['id'] == 'supportive-care':
            supportive = '''<div class="supportive-project"><p class="project-label">Project focus</p><h3>Genetic counseling and testing in community oncology</h3><p>Assess the landscape, identify implementation barriers, co-design strategies, and develop an implementation blueprint to improve uptake.</p></div><div class="supportive-project"><p class="project-label">Project focus</p><h3>Serious illness conversations in geriatric oncology</h3><p>Study the implementation of serious illness conversations through a hybrid effectiveness–implementation type 1 trial.</p></div>'''
        sections.append(f'<section class="research-area" id="{e(area["id"])}"><h2>{e(area["title"])}</h2><p class="area-intro">{e(area["description"])}</p>{focus}{projects}{supportive}</section>')
    future = f'<section class="future-directions" id="future-directions"><p class="eyebrow">Looking ahead</p><h2>Future directions</h2>{items(DATA["future"])}</section>'
    return f'''<div class="container page-heading"><p class="eyebrow">TRACC Lab</p><h1>Research</h1><p class="page-intro">{e(DATA['goal'])}</p></div><div class="container research-layout"><nav class="research-nav" aria-label="Research areas"><p>On this page</p>{sidebar}<a href="#future-directions">Future directions</a></nav><div class="research-main">{''.join(sections)}{future}</div></div><div class="container inline-contact"><h2>Have an implementation research question?</h2><p>We welcome conversations about cancer screening, supportive care, and implementation support.</p><a class="button" href="index.html#contact">Contact the lab</a></div>'''


def person(person, pi=False):
    classes = 'person pi-profile' if pi else 'person'
    picture = f'<img class="person-photo" src="{e(person["photo"])}" width="{230 if pi else 144}" height="{300 if pi else 180}" alt="{e(person["name"])}" loading="lazy">' if person.get('photo') else '<div class="person-photo person-photo--empty" aria-hidden="true"></div>'
    name = e(person['name']) + (f'<span>, {e(person["degree"])}</span>' if pi and person.get('degree') else '')
    level = 'h2' if pi else 'h3'
    links = f'<div class="profile-links"><a class="text-link" href="{e(DATA["scholar"])}" target="_blank" rel="noopener noreferrer">Google Scholar</a><a class="text-link" href="https://www.urmc.rochester.edu/people/112365270-junqiang-zhao" target="_blank" rel="noopener noreferrer">University profile</a></div>' if pi else ''
    return f'<article class="{classes}" id="{e(person["name"].lower().replace(" ", "-"))}">{picture}<div class="person-copy"><p class="person-role">{e(person["role"])}</p><{level}>{name}</{level}>{paragraphs(person["bio"])}{links}</div></article>'


def people():
    pi = next(p for p in DATA['people'] if p['group'] == 'pi')
    groups = []
    for group_id, title in [('graduate', 'Graduate research assistants'), ('undergraduate', 'Undergraduate research assistant'), ('management', 'Research management')]:
        members = sorted(
            (p for p in DATA['people'] if p['group'] == group_id),
            key=lambda p: (p['name'].rsplit(' ', 1)[-1].casefold(), p['name'].casefold()),
        )
        profiles = ''.join(person(p) for p in members)
        groups.append(f'<section class="people-group" aria-labelledby="{group_id}-heading"><h2 id="{group_id}-heading">{title}</h2>{profiles}</section>')
    return f'''<div class="container page-heading"><p class="eyebrow">TRACC Lab</p><h1>People</h1><p class="page-intro">Our research team brings together expertise in implementation science, decision support, and public health research.</p></div><div class="container people-content">{person(pi, True)}{''.join(groups)}</div><div class="container inline-contact"><h2>Connect with the TRACC team</h2><p>Interested in our research or potential collaborations?</p><a class="button" href="index.html#contact">Get in touch</a></div>'''


def news():
    n = DATA['news']
    return f'''<div class="container page-heading"><p class="eyebrow">TRACC Lab</p><h1>Lab news</h1></div><section class="container news-page" aria-label="Lab news"><article class="news-article" id="surgery-symposium-2026"><div><p class="eyebrow">{e(n['year'])} · Research presentation</p><h2>{e(n['title'])}</h2><p>Yufei Jia presented research at the Department of Surgery Scientific Symposium in 2026.</p><a class="text-link" href="people.html#yufei-jia">Meet Yufei</a></div><figure><img src="{e(n['photo'])}" width="503" height="670" alt="Yufei Jia standing beside a research poster at the Department of Surgery Scientific Symposium" loading="eager"><figcaption>{e(n['caption'])}</figcaption></figure></article></section>'''


page('index.html', 'TRACC Lab | Translating Research into Action in Cancer Care', DATA['mission'], home())
page('research.html', 'Research | TRACC Lab', DATA['goal'], research())
page('people.html', 'People | TRACC Lab', 'Meet the TRACC Lab research team, led by Junqiang Zhao at the University of Rochester.', people())
page('news.html', 'Lab News | TRACC Lab', 'Research presentations and news from the TRACC Lab.', news())
print('Built index.html, research.html, people.html, and news.html.')
