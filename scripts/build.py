"""Build the four-section monoloco static site from edited copy and selected media."""
from pathlib import Path
from html import escape as esc
from datetime import datetime, timezone
import json
import shutil
import posixpath
from copy import deepcopy
from site_data_en import localized_content, ALT
from site_i18n import translate_html, MISSING
from site_zh import localize_chinese_html
from site_data import PROJECTS, WORKSHOPS, OBJECTS, MEMBERS

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
MEDIA = json.loads((ROOT / 'content/media.json').read_text())
PREVIEWS = json.loads((ROOT / 'content/previews.json').read_text())
DOORS = json.loads((ROOT / 'content/works.json').read_text())
DOMAIN = (DOCS / 'CNAME').read_text().strip() if (DOCS / 'CNAME').exists() else ''
BASE_PATH = '/' if DOMAIN else '/monoloco.art/'
PUBLIC_URL = f'https://{DOMAIN}' if DOMAIN else 'https://waanng.github.io/monoloco.art'
NAV = [('projects','艺术项目','Projects'),('workshops','动手工坊','Workshops'),('objects','文创作品','Products'),('about','关于我们','About')]
OUTPUTS = {}
LANG = 'zh-CN'
CURRENT_PATH = 'index.html'
ZH_CONTENT = deepcopy((PROJECTS, WORKSHOPS, OBJECTS, MEMBERS, DOORS))

def assets(base):
    if LANG != 'en':return base
    return BASE_PATH if base.startswith('/') else '../'+base

ARROW = '<span class="arrow" aria-hidden="true">↗</span>'

def url(path, base):
    return base + path + ('index.html' if path.endswith('/') else '')

def preview_picture(group,key,base,alt,width,height,attrs,sizes):
    preview=PREVIEWS[f'{group}/{key}']
    folder=assets(base)+f'assets/images/{group}/'
    candidates=', '.join(f'{folder}{v["file"]} {v["width"]}w' for v in preview['sources'])
    return f'<picture><source type="image/webp" srcset="{candidates}" sizes="{sizes}"><img src="{folder}{preview["fallback"]}" alt="{esc(alt)}" width="{width}" height="{height}" {attrs} decoding="async"></picture>'

def image(key, base, eager=False, sizes='(max-width: 600px) calc(100vw - 40px), 640px'):
    attrs = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    if key == 'doors':
        w=DOORS[0]
        return preview_picture('four-doors',w['id'],base,w['altZh'],w['width'],w['height'],attrs,sizes)
    m=MEDIA[key]
    return preview_picture('editorial',key,base,ALT[key] if LANG=='en' else m['alt'],m['width'],m['height'],attrs,sizes)

def arrow_link(href, text):
    return f'<a class="arrow-link" href="{href}">{esc(text)} {ARROW}</a>'

def page(title, description, body, base='./', current='', gallery=False):
    nav=''
    for slug,zh,en in NAV:
        active=' aria-current="page"' if current==slug else ''
        nav+=f'<a href="{url(slug+"/",base)}"{active}>{en if LANG=="en" else zh}</a>'
    footnav=''.join(f'<a href="{url(slug+"/",base)}">{zh}</a>' for slug,zh,en in NAV)
    asset_base=assets(base)
    script=f'<script src="{asset_base}assets/js/gallery.js" defer></script>' if gallery else ''
    local_path=('en/' if LANG=='en' else '')+CURRENT_PATH
    counterpart=('' if LANG=='en' else 'en/')+CURRENT_PATH
    switch=posixpath.relpath(counterpart,posixpath.dirname(local_path) or '.')
    if CURRENT_PATH=='404.html':switch=BASE_PATH+counterpart
    self_link=BASE_PATH+local_path if CURRENT_PATH=='404.html' else posixpath.basename(CURRENT_PATH)
    robots='<meta name="robots" content="noindex">' if CURRENT_PATH=='404.html' else ''
    canonical=PUBLIC_URL+'/'+local_path.removesuffix('index.html')
    zh_url=PUBLIC_URL+'/'+CURRENT_PATH.removesuffix('index.html')
    en_url=PUBLIC_URL+'/en/'+CURRENT_PATH.removesuffix('index.html')
    language_links=f'''<div class="language-switch" aria-label="Language"><a href="{switch if LANG=="en" else self_link}" lang="zh-CN"{' aria-current="true"' if LANG!="en" else ' data-language="zh-CN"'}>中文</a><span aria-hidden="true">/</span><a href="{self_link if LANG=="en" else switch}" lang="en"{' aria-current="true"' if LANG=="en" else ' data-language="en"'}>EN</a></div>'''
    return f'''<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f5f3ee">
{robots}
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'en_US' if LANG=='en' else 'zh_CN'}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="zh-CN" href="{zh_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{zh_url}">
<meta property="og:image" content="{PUBLIC_URL}/assets/images/four-doors/doors-01.jpg">
<link rel="icon" href="{asset_base}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{asset_base}assets/css/site.css">
<link rel="stylesheet" href="{asset_base}assets/css/editorial.css">
<link rel="stylesheet" href="{asset_base}assets/css/i18n.css">
<script src="{asset_base}assets/js/language.js" defer></script>
{script}
</head>
<body id="top">
<a class="skip" href="#main">跳到正文</a>
<header class="masthead wrap"><a class="wordmark" href="{base}index.html" aria-label="monoloco 首页">monoloco<span>.</span></a><div class="header-links"><nav aria-label="主导航">{nav}</nav>{language_links}</div></header>
{body}
<footer class="footer-four wrap"><div class="footer-top"><a class="footer-brand" href="{base}index.html">monoloco.</a><nav aria-label="页脚导航">{footnav}</nav></div><div class="footer-bottom"><span>观察 · 记录 · 制作 · 分享</span><a href="#top">回到顶部 ↑</a></div></footer>
</body>
</html>
'''

def breadcrumb(base, section, title):
    return f'<a class="breadcrumb" href="{url(section+"/",base)}"><span aria-hidden="true">←</span> 返回{title}</a>'

def heading(kicker,title,subtitle,description):
    return f'<section class="project-head"><div><div class="eyebrow accent">{kicker}</div><h1>{title}<span class="accent">。</span></h1><p class="subtitle">{subtitle}</p></div><p class="statement">{description}</p></section>'

def viewer():
    return '''<dialog class="viewer" id="viewer" aria-labelledby="viewer-title"><div class="viewer-shell"><div class="viewer-top"><span class="eyebrow">MONOLOCO / 作品浏览</span><button type="button" data-close aria-label="关闭大图">关闭 ×</button></div><div class="viewer-stage"><img alt=""><p class="viewer-error" role="alert" hidden>图片暂时无法加载，请稍后重试。</p></div><div class="viewer-bottom"><button type="button" data-previous aria-label="上一组作品">← 上一组</button><div class="viewer-info" aria-live="polite" aria-atomic="true"><div id="viewer-title"></div><span id="viewer-count"></span></div><button type="button" data-next aria-label="下一组作品">下一组 →</button></div></div></dialog>'''

def media_figure(key,base,caption='',eager=False,cls=''):
    m=MEDIA[key]
    title=caption or (ALT[key] if LANG=='en' else m['alt'])
    return f'<figure class="work {cls}"><a href="{assets(base)}assets/images/editorial/{m["fallback"]}" data-work="{key}" data-title="{esc(title)}" aria-label="放大观看：{esc(title)}">{image(key,base,eager)}<span class="open-label" aria-hidden="true">放大观看 ↗</span></a><figcaption>{esc(caption)}</figcaption></figure>'

def card(item,section,base,index=None):
    path=url(f'{section}/{item["slug"]}/',base)
    kind=item.get('kind',item.get('tag',''))
    if section=='workshops':
        kind='筹备中 · '+kind
    n=f'<span class="card-number">{index:02d}</span>' if index else ''
    sizes='(max-width:420px) calc(100vw - 40px), (max-width:700px) calc((100vw - 60px) / 2), 420px'
    return f'<article class="editorial-card card-{section}"><a href="{path}" class="card-media" data-cover="{esc(item["cover"])}" aria-label="查看{esc(item["title"])}">{image(item["cover"],base,sizes=sizes)}</a><div class="card-caption"><div><p class="card-kind">{esc(kind)}</p><h3><a href="{path}">{esc(item["title"])}</a></h3><p class="card-subtitle">{esc(item["subtitle"])}</p></div>{n}</div></article>'

def section_top(number,en,title,href=None,label=None):
    action=arrow_link(href,label) if href else ''
    return f'<div class="section-top"><div><div class="eyebrow accent">{number} / {en}</div><h2 class="section-title">{title}</h2></div>{action}</div>'

def home():
    base='./'
    featured=['four-doors','qianmo','five-kilometers']
    art=''.join(card(next(p for p in PROJECTS if p['slug']==slug),'projects',base,i+1) for i,slug in enumerate(featured))
    workshops=''.join(card(w,'workshops',base,i+1) for i,w in enumerate(WORKSHOPS))
    objects=''.join(card(o,'objects',base,i+1) for i,o in enumerate(OBJECTS))
    people=''.join(f'<a class="people-preview" href="./about/index.html#{p["image"]}">{image(p["image"],base)}<span>{p["name"]}</span></a>' for p in MEMBERS)
    body=f'''<main id="main">
<section class="hero hero-four wrap"><div class="hero-copy"><div class="eyebrow">MONOLOCO / 艺术与生活实践</div><h1>看见日常，<br>一起创造<span class="stop">。</span></h1><p>用摄影与速写记录观察，<br>以手作和设计，让创作进入生活。</p>{arrow_link('./projects/index.html','浏览艺术项目')}</div><figure class="hero-art"><a class="art-link" href="./projects/four-doors/index.html" aria-label="进入四门集">{image('doors',base,True)}</a><figcaption><span>四门集 <span class="muted">/ 门之四重奏</span></span><span>SELECTED PROJECT</span></figcaption></figure></section>
<div class="hero-meta wrap"><span>{"ART IN EVERYDAY LIFE" if LANG=="en" else "影像可持续 / IMAGE & EVERYDAY"}</span><span class="intro">三个人，从观察、记录到共同制作。</span><span>向下浏览 ↓</span></div>
<section class="section featured wrap" id="works">{section_top('01','ART PROJECTS','艺术项目','./projects/index.html','全部项目')}<div class="cards-three">{art}</div></section>
<section class="workshop-home"><div class="wrap section">{section_top('02','HANDS-ON WORKSHOPS','动手工坊','./workshops/index.html','了解工坊')}<p class="section-intro">从观看到动手。一起做一本本子，让光留下影子，走近胶片显影的过程。</p><div class="cards-three">{workshops}</div></div></section>
<section class="section wrap">{section_top('03','PRODUCTS','文创作品','./objects/index.html','查看作品')}<p class="section-intro">让一幅画、一段旅程，成为可以带进日常的物件。</p><div class="cards-two">{objects}</div></section>
<section class="collective-home"><div class="wrap collective-grid"><div><div class="eyebrow accent">04 / ABOUT US</div><h2>三个人，<br>共同的目光。</h2><p>monoloco 从社区营造出发，走向策展、创作与文创设计。以影像可持续为线索，在记录与制作之间持续探索。</p>{arrow_link('./about/index.html','认识我们')}</div><div class="people-previews">{people}</div></div></section>
</main>'''
    return page('monoloco — 艺术与生活实践','艺术项目、动手工坊与文创作品。monoloco 以摄影、速写、手工本和设计，记录日常并共同创造。',body)

def index_page(section,title,en,subtitle,intro,items):
    base='../'
    grid='cards-two' if section=='objects' else 'cards-three'
    cards=''.join(card(item,section,base,i+1) for i,item in enumerate(items))
    body=f'<main id="main" class="wrap">{heading(en,title,subtitle,intro)}<section class="{grid} catalog" aria-label="{title}列表">{cards}</section></main>'
    return page(f'{title} — monoloco',intro,body,base,section)

def project_detail(project):
    base='../../'
    is_doors=project['slug']=='four-doors'
    head=heading('ART PROJECT / '+project['kind'],project['title'],project['subtitle'],project['intro'])
    byline=f'<div class="gallery-bar"><span>{esc(project["author"])}</span><span>点击作品，放大观看 ↗</span></div>'
    figures=''
    if is_doors:
        for i,w in enumerate(DOORS):
            folder=assets(base)+'assets/images/four-doors/'
            pic=preview_picture('four-doors',w['id'],base,w['altZh'],w['width'],w['height'],f'loading="{"eager" if i<2 else "lazy"}"','(max-width:600px) calc(100vw - 40px), 640px')
            figures+=f'<figure class="work" id="{w["id"]}"><a href="{folder}{w["fallback"]}" data-work="{w["id"]}" data-title="{esc(w["titleZh"])}" aria-label="放大观看：{esc(w["titleZh"])}">{pic}<span class="open-label" aria-hidden="true">放大观看 ↗</span></a><figcaption><span class="index">{i+1:02d}</span><span>{esc(w["titleZh"])}</span><small>门之四重奏</small></figcaption></figure>'
        content=f'<section class="gallery" aria-label="四门集作品">{figures}</section>'
    else:
        for i,(key,caption) in enumerate(project['media']):
            figures+=media_figure(key,base,caption,i<2)
        paragraphs=''.join(f'<p>{p}</p>' for p in project['paragraphs'])
        content=f'<div class="reading-intro"><p class="quote">{project["quote"]}</p><div>{paragraphs}</div></div><section class="gallery narrative-gallery" aria-label="{project["title"]}作品">{figures}</section>'
    related=project.get('related')
    if related:
        ending=arrow_link(url(related[0],base),related[1])
    else:
        ending=arrow_link(url('projects/',base),'继续浏览艺术项目')
    body=f'<main id="main" class="wrap">{breadcrumb(base,"projects","艺术项目")}{head}{byline}{content}<div class="project-end"><p>停下来，再看一眼。</p>{ending}</div></main>{viewer()}'
    return page(f'{project["title"]} — monoloco',project['intro'],body,base,'projects',True)

def workshop_detail(w):
    base='../../'
    stages=''.join(f'<div class="process-step"><span class="eyebrow accent">{n}</span><h3>{title}</h3><p>{text}</p></div>' for n,title,text in w['stages'])
    opening=media_figure(w['cover'],base,w['subtitle'],True)
    extras=''
    if w['slug']=='handmade-books':
        examples=''.join(media_figure(key,base,cap) for key,cap in [('notebook-writing','一句话，也可以是记录的开始。'),('notebook-coffee','把文字、速写和贴纸放在一起。'),('notebook-photo','为照片留一个位置。'),('notebook-map','把走过的路画下来。')])
        bindings=''.join(media_figure(f'binding-process-{i}',base,caption) for i,caption in [(1,'缝线本'),(2,'环装本'),(3,'风琴本')])
        extras=f'<section class="chapter"><div class="chapter-heading"><div class="eyebrow accent">MAKE A BOOK</div><h2>先做一本。</h2><p>让散页以不同的方式相连。每期工坊选取的结构与材料，将在场次中说明。</p></div><div class="cards-three instruction-gallery">{bindings}</div></section><section class="chapter" id="fill-it"><div class="chapter-heading"><div class="eyebrow accent">FILL IT WITH LIFE</div><h2>如何填满它？</h2><p>从朋友的废包装纸开始，裁成小小的方形，找身边的材料做封面。带在身边，轻巧纤薄，涂涂画画，没有压力。走过的路、见过的景、探过的店、遇到的人，慢慢成为一本自己的记忆。</p></div><div class="gallery">{examples}</div>{arrow_link(url("projects/journey-notes/",base),"看看我们仨的旅途")}</section>'
        extras+=f'<section class="chapter split-chapter"><div><div class="eyebrow accent">READY TO GO</div><h2>带上它，去记录。</h2><p>一个随身包，几支笔，一本小本子，再带上顺手的记录工具。不必准备得很复杂，出门就能把眼前的日常留下来。</p></div>{media_figure("notebook-kit",base,"包包、纸笔与随身记录工具。")}</section>'
    elif w['slug']=='cyanotype':
        steps=''.join(media_figure(f'cyanotype-process-{i}',base,cap) for i,cap in [(1,'材料准备与涂布'),(2,'避光晾干与构图准备'),(3,'曝光与水洗显影')])
        extras=f'<section class="chapter"><div class="chapter-heading"><div class="eyebrow accent">THE MAKING PROCESS</div><h2>光，慢慢留下痕迹。</h2><p>用手绘图认识蓝晒的基本过程。实际材料与操作由现场方案和指导决定。</p></div><div class="cards-three instruction-gallery">{steps}</div></section>'
    else:
        extras=f'<section class="chapter split-chapter"><div><div class="eyebrow accent">OUR FILM PRACTICE</div><h2>从相机到影像。</h2><p>胶片也在我们的创作里。相机、底片和等待，让记录拥有另一种速度。</p>{arrow_link(url("projects/five-kilometers/",base),"看看胶片相关的城市观察")}</div>{media_figure("five-window",base,"窗边，留在胶片里的光。")}</section>'
    body=f'''<main id="main" class="wrap">{breadcrumb(base,'workshops','动手工坊')}{heading('HANDS-ON WORKSHOP',w['title'],w['subtitle'],w['intro'])}<div class="gallery-bar"><span class="status-dot">筹备中</span><span>{w['tag']}</span></div><div class="workshop-opening">{opening}<aside><div class="eyebrow accent">TAKE PART / 一起动手</div><h2>不止观看，<br>也亲手试试看。</h2><p>{w['outcome']}</p><p class="muted">{w['preparation']}</p></aside></div><section class="process-grid" aria-label="工坊内容">{stages}</section>{extras}<section class="participation"><div><div class="eyebrow accent">UPCOMING / 参与方式</div><h2>下一次，一起做。</h2><p>工坊正在筹备。具体时间、地点、主讲人、材料和参与方式，将在场次确定后公布。</p></div><div><p>如果你是文化空间、社区或活动组织者，欢迎和我们交流工坊合作。</p>{arrow_link(url("about/",base)+"#contact","工坊合作与咨询")}</div></section></main>{viewer()}'''
    return page(f'{w["title"]} — monoloco',w['intro'],body,base,'workshops',True)

def object_detail(o):
    base='../../'
    show_cover=o.get('show_cover',True)
    opening=f'<div class="object-hero">{media_figure(o["cover"],base,o["subtitle"],True)}</div>' if show_cover else ''
    chapters=''
    for key,kicker,title,text in o['sections']:
        chapters+=f'<section class="chapter object-chapter"><div class="chapter-heading"><div class="eyebrow accent">{kicker}</div><h2>{title}</h2><p>{text}</p></div>{media_figure(key,base,title,not show_cover and key==o["sections"][0][0])}</section>'
    if o['slug']=='vinyl-notebook':
        cities=['利物浦','阿姆斯特丹','柏林','布拉格','维也纳','米兰','巴黎']
        cities_html=''.join(media_figure(f'vinyl-city-{i}',base,city) for i,city in enumerate(cities,1))
        chapters+=f'<section class="chapter"><div class="chapter-heading"><div class="eyebrow accent">03 / CITIES & NOTES</div><h2>七座城市，七段音乐记忆。</h2><p>城市速写进入唱片的圆形结构，与音乐主题一起构成内页。翻过图像，空白的纸面等待新的记录。</p></div><div class="city-grid">{cities_html}</div></section><section class="chapter object-chapter"><div class="chapter-heading"><div class="eyebrow accent">04 / DETAILS</div><h2>从封面延续到腰封。</h2><p>把旅行路线、主题文字与唱片的视觉线索放在一起，成为一本完整的伴手本。</p></div>{media_figure("vinyl-band",base,"腰封图形局部")}</section>'
    details=''.join(f'<div><dt>{label}</dt><dd>{value}</dd></div>' for label,value in o['details'])
    body=f'<main id="main" class="wrap">{breadcrumb(base,"objects","文创作品")}{heading("PRODUCT DESIGN",o["title"],o["subtitle"],o["intro"])}<div class="gallery-bar"><span>{o["kind"]}</span><span>设计方案 / DESIGN STUDY</span></div>{opening}{chapters}<dl class="object-facts">{details}</dl><div class="project-end"><p>{o["closing"]}</p>{arrow_link(url("about/",base)+"#contact","交流设计合作")}</div></main>{viewer()}'
    return page(f'{o["title"]} — monoloco',o['intro'],body,base,'objects',True)

def about():
    base='../'
    people=''
    for p in MEMBERS:
        instagram='<p class="member-handle"><a href="https://www.instagram.com/waanng/">Instagram · @waanng ↗</a></p>' if p['image']=='wangan' else ''
        people+=f'<article class="member" id="{p["image"]}"><div class="member-image">{image(p["image"],base)}</div><div class="eyebrow accent">{p["line"]}</div><h3>{p["name"]}</h3><p>{p["bio"]}</p><p class="member-handle">小红书 · {p["handle"]}</p>{instagram}{arrow_link(url("projects/"+p["project"]+"/",base),"查看相关作品")}</article>'
    history=''.join(f'<li>{x}</li>' for x in ['白塔寺街区 · 旧物改造花园与“药局”','胡同美术馆 · 插画展','《杯子在溜达》· CITYWALK 速写巡展','宣武门胡同 · monoloco 快闪咖啡馆'])
    body=f'''<main id="main" class="wrap"><section class="about-head"><div><div class="eyebrow accent">ABOUT MONOLOCO / 关于我们</div><h1>三个人，<br>共同的目光<span class="accent">。</span></h1></div><div class="about-copy"><p>monoloco 始于 2017 年，从社区营造出发，逐渐走向策展、文创设计与持续的艺术实践。</p><p>我们用胶片、速写和手工本记录城市，也通过共同制作，让创作进入日常。影像可持续，是连接这些探索的一条线索。</p></div></section><section class="members" aria-label="三位成员">{people}</section><section class="chapter about-practice"><div class="chapter-heading"><div class="eyebrow accent">OUR PRACTICE</div><h2>从街区出发，<br>让创作继续发生。</h2><p>我们曾在胡同里做花园、办展览、记录行走，也尝试用一间快闪咖啡馆让人相遇。那些实践留下的线索，继续进入今天的作品、工坊与物件。</p></div><ul class="history-list">{history}</ul></section><section class="contact-section" id="contact"><div><div class="eyebrow accent">LET'S MAKE SOMETHING</div><h2>一起做些有意思的事。</h2><p>欢迎交流工坊邀请、文化空间合作、展览与文创设计。</p></div><div class="contact-handles"><div><span>小红书</span><strong>MONOLOCO</strong></div><div><span>微博</span><strong>MONOLOCO生活实验</strong></div><p>可在相应平台搜索以上账号名，与我们联系。</p></div></section></main>'''
    return page('关于我们 — monoloco','认识 LZ、KASA 和王安。monoloco 从社区营造出发，以摄影、速写、动手工坊与文创设计持续探索。',body,base,'about')

def render_locale():
    emit('index.html', lambda: home())
    emit('projects/index.html', lambda: index_page('projects','艺术项目','ART PROJECTS','观察，记录，留下片刻。','从门头、土壤、城市与旅途出发，用摄影、速写和文字，留下与世界相遇的方式。',PROJECTS))
    emit('workshops/index.html', lambda: index_page('workshops','动手工坊','HANDS-ON WORKSHOPS','从观看，到一起动手。','把创作的方法带到一起。做一本手工本，尝试蓝晒，走近胶片显影，让自己的日常成为作品的起点。',WORKSHOPS))
    emit('objects/index.html', lambda: index_page('objects','文创作品','PRODUCTS','让创作，进入日常。','从城市速写到随身本，从校园长卷到礼品杯。让创作离开纸面，在日常物件中继续生长。',OBJECTS))
    for p in PROJECTS:emit(f'projects/{p["slug"]}/index.html', lambda: project_detail(p))
    for w in WORKSHOPS:emit(f'workshops/{w["slug"]}/index.html', lambda: workshop_detail(w))
    for o in OBJECTS:emit(f'objects/{o["slug"]}/index.html', lambda: object_detail(o))
    emit('about/index.html', lambda: about())
    body=f'<main id="main" class="wrap error-page"><div class="eyebrow accent">404 / PAGE NOT FOUND</div><h1>走到了另一扇门。</h1><p>这个页面暂时不存在。回到作品，继续浏览。</p>{arrow_link((BASE_PATH+"en/" if LANG=="en" else BASE_PATH)+"index.html","返回首页")}</main>'
    emit('404.html', lambda: page('页面未找到 — monoloco','回到 monoloco 作品与共同实践。',body,BASE_PATH+('en/' if LANG=='en' else '')))

def emit(path, render):
    global CURRENT_PATH
    CURRENT_PATH=path
    content=render()
    OUTPUTS[('en/' if LANG=='en' else '')+path]=translate_html(content) if LANG=='en' else localize_chinese_html(content)

def build():
    global LANG, PROJECTS, WORKSHOPS, OBJECTS, MEMBERS, DOORS
    OUTPUTS.clear()
    MISSING.clear()
    for LANG in ['zh-CN','en']:
        PROJECTS,WORKSHOPS,OBJECTS,MEMBERS,DOORS=deepcopy(ZH_CONTENT) if LANG=='zh-CN' else localized_content(*ZH_CONTENT)
        render_locale()
    if MISSING:raise ValueError('Missing English translations: '+repr(sorted(MISSING)))
    for name,content in OUTPUTS.items():
        path=DOCS/name
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(content)
    sitemap=''.join('<url><loc>'+PUBLIC_URL+'/'+name.removesuffix('index.html')+'</loc></url>' for name in OUTPUTS if not name.endswith('404.html'))
    (DOCS/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+sitemap+'</urlset>\n')
    (DOCS/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+PUBLIC_URL+'/sitemap.xml\n')
    preview=ROOT/'opendesign/mockups/monoloco'
    shutil.copytree(DOCS,preview,dirs_exist_ok=True)
    sections=[]
    for folder,label in [('mockups','Mockups'),('design-systems','Design Systems')]:
        groups=[]
        root=ROOT/'opendesign'/folder
        root.mkdir(parents=True,exist_ok=True)
        for group in sorted(root.iterdir()):
            if not group.is_dir():continue
            files=sorted(group.rglob('*.html') if folder=='mockups' else (p for p in group.rglob('*') if p.is_file()))
            if files:groups.append({'slug':group.name,'files':[{'label':str(p.relative_to(group)),'path':str(p.relative_to(ROOT/'opendesign'))} for p in files]})
        sections.append({'id':folder,'label':label,'groups':groups})
    (ROOT/'opendesign/manifest.json').write_text(json.dumps({'generated':datetime.now(timezone.utc).isoformat(),'sections':sections},ensure_ascii=False,indent=2)+'\n')
    print(f'Built {len(OUTPUTS)} static pages and refreshed the OpenDesign preview.')

if __name__=='__main__':build()
