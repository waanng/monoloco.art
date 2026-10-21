"""Generate the static site using only the Python standard library."""
from pathlib import Path
from html import escape as esc
from datetime import datetime, timezone
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
WORKS = json.loads((ROOT / 'content/works.json').read_text())
DOMAIN = (DOCS / 'CNAME').read_text().strip() if (DOCS / 'CNAME').exists() else ''
BASE_PATH = '/' if DOMAIN else '/monoloco.art/'
PUBLIC_URL = f'https://{DOMAIN}' if DOMAIN else 'https://waanng.github.io/monoloco.art'

def image(work, base, eager=False, sizes='(max-width: 600px) calc(100vw - 40px), 600px'):
    folder = base + 'assets/images/four-doors/'
    attrs = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return f'''<picture><source type="image/webp" srcset="{folder}{work['thumbnail']} 640w, {folder}{work['image']} 1080w" sizes="{sizes}"><img src="{folder}{work['fallback']}" alt="{esc(work['altZh'])}" width="{work['width']}" height="{work['height']}" {attrs} decoding="async"></picture>'''

def page(title, description, body, base='./', current='', gallery=False):
    work_current = ' aria-current="page"' if current == 'works' else ''
    about_current = ' aria-current="page"' if current == 'about' else ''
    script = f'<script src="{base}assets/js/gallery.js" defer></script>' if gallery else ''
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f5f3ee">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="zh_CN">
<meta property="og:image" content="{PUBLIC_URL}/assets/images/four-doors/doors-01.jpg">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{base}assets/css/site.css">
{script}
</head>
<body id="top">
<a class="skip" href="#main">跳到正文</a>
<header class="masthead wrap">
<a class="wordmark" href="{base}index.html" aria-label="monoloco 首页">monoloco<span>.</span></a>
<nav aria-label="主导航"><a href="{base}index.html#works"{work_current}>作品 <small>Works</small></a><a href="{base}about/index.html"{about_current}>关于 <small>About</small></a></nav>
</header>
{body}
<footer class="site-footer wrap"><a class="footer-brand" href="{base}index.html">monoloco.</a><div class="footer-end"><span>三人艺术团体 · 作品与共同的观察</span><a href="#top">回到顶部 ↑</a></div></footer>
</body>
</html>
'''

def home():
    base = './'
    previews = ''
    for w in WORKS[:3]:
        previews += f'''<figure><a class="art-link" href="./projects/four-doors/index.html#{w['id']}" aria-label="观看四门集：{esc(w['titleZh'])}">{image(w, base, sizes='(max-width: 600px) 45vw, 400px')}</a><figcaption class="caption"><span>{esc(w['titleZh'])}</span><span class="index">{w['order']:02d}</span></figcaption></figure>'''
    body = f'''<main id="main">
<section class="hero wrap" aria-labelledby="hero-title">
<div class="hero-copy"><div class="eyebrow">MONOLOCO / ART COLLECTIVE</div><h1 id="hero-title">在门与门<br>之间<span class="stop">。</span></h1><p>四扇门，四种形态。<br>在不同的地方，寻找相通的风格与记忆。</p><a class="arrow-link" href="./projects/four-doors/index.html">走进四门集 <span class="arrow" aria-hidden="true">↗</span></a></div>
<figure class="hero-art"><a class="art-link" href="./projects/four-doors/index.html" aria-label="进入四门集项目">{image(WORKS[0],base,True)}</a><figcaption><span>四门集 <span class="muted">/ 门之四重奏</span></span><span>FOUR DOORS, A QUARTET</span></figcaption></figure>
</section>
<div class="hero-meta wrap"><span>摄影 · 地方 · 日常观察</span><span class="intro">monoloco，一个由三人组成的艺术团体。</span><span>向下浏览 ↓</span></div>
<section id="works" class="section featured wrap" aria-labelledby="works-title"><div class="section-top"><div><div class="eyebrow accent">SELECTED PROJECT / 作品</div><h2 class="section-title" id="works-title">四门集</h2></div><span class="section-count">01 — 门之四重奏</span></div><div class="project-grid">{previews}</div><div class="project-bottom"><p>门连接建筑的内与外。四幅影像彼此并置，记录一处地方，也留住一次相遇。</p><a class="arrow-link" href="./projects/four-doors/index.html">浏览完整选集 <span class="arrow" aria-hidden="true">↗</span></a></div></section>
<section class="about-strip" aria-labelledby="about-title"><div class="wrap"><div><div class="eyebrow">ABOUT MONOLOCO</div><h2 id="about-title">三个人，共同的目光。</h2></div><div><p>这里收录 monoloco 的作品。<br>从一扇门开始，看看日常还有哪些值得驻足的地方。</p><a class="arrow-link" href="./about/index.html">关于我们 <span class="arrow" aria-hidden="true">↗</span></a></div></div></section>
</main>'''
    return page('monoloco — 三人艺术团体', 'monoloco 是一个由三人组成的艺术团体。进入四门集，在门与门之间观看地方、建筑与日常。', body)

def project():
    base = '../../'
    figures = ''
    for i, w in enumerate(WORKS):
        folder = base + 'assets/images/four-doors/'
        figures += f'''<figure class="work" id="{w['id']}"><a href="{folder}{w['fallback']}" data-work="{w['id']}" data-title="{esc(w['titleZh'])}" aria-label="放大观看：{esc(w['titleZh'])}">{image(w,base,i<2)}<span class="open-label" aria-hidden="true">放大观看 ↗</span></a><figcaption><span class="index">{i+1:02d}</span><span>{esc(w['titleZh'])}</span><small>门之四重奏</small></figcaption></figure>'''
    body = f'''<main id="main" class="wrap">
<a class="breadcrumb" href="../../index.html#works"><span aria-hidden="true">←</span> 返回作品</a>
<section class="project-head" aria-labelledby="project-title"><div><div class="eyebrow accent">PHOTOGRAPHIC SERIES / 摄影项目</div><h1 id="project-title">四门集<span class="accent">。</span></h1><p class="subtitle">门之四重奏</p></div><p class="statement">门，连接着建筑的内部与外部。<br>在不同地方，四张门头被放在一起：形式各异，又有相通的风格与主题。<br>以一组影像，记住一个地方。</p></section>
<div class="gallery-bar"><span>SELECTED WORKS / 精选 {len(WORKS):02d} 组</span><span>点击作品，进入大图观看 ↗</span></div>
<section class="gallery" aria-label="四门集精选作品">{figures}</section>
<div class="project-end"><p>一扇门，也是一种观看。</p><a class="arrow-link" href="../../about/index.html">认识 monoloco <span class="arrow" aria-hidden="true">↗</span></a></div>
</main>
<dialog class="viewer" id="viewer" aria-labelledby="viewer-title"><div class="viewer-shell"><div class="viewer-top"><span class="eyebrow">四门集 / 门之四重奏</span><button type="button" data-close aria-label="关闭大图">关闭 ×</button></div><div class="viewer-stage"><img alt=""><p class="viewer-error" role="alert" hidden>图片暂时无法加载，请稍后重试。</p></div><div class="viewer-bottom"><button type="button" data-previous aria-label="上一组作品">← 上一组</button><div class="viewer-info" aria-live="polite" aria-atomic="true"><div id="viewer-title"></div><span id="viewer-count"></span></div><button type="button" data-next aria-label="下一组作品">下一组 →</button></div></div></dialog>'''
    return page('四门集 · 门之四重奏 — monoloco', f'门连接建筑的内与外。浏览四门集的 {len(WORKS)} 组四联摄影，在不同的形态之间寻找相通的风格与记忆。', body, base, 'works', True)

def about():
    base = '../'
    body = f'''<main id="main" class="wrap"><section class="about-head" aria-labelledby="about-heading"><div><div class="eyebrow accent">ABOUT / 关于我们</div><h1 id="about-heading">三个人，<br>共同的目光<span class="accent">。</span></h1></div><div class="about-copy"><p>monoloco 是一个由三人组成的艺术团体。</p><p>这里是一份持续展开的作品档案。<br>从《四门集》开始，记录不同地方的建筑入口，<br>让独立的影像在并置中相遇。</p></div></section><div class="about-divider"></div><figure class="about-photo">{image(WORKS[2],base,True)}<figcaption><div class="eyebrow">OUR FIRST CHAPTER / 作品档案</div><h2>从四扇门开始。</h2><p>一组四张，各不相同。<br>相通的风格、主题与地方记忆，<br>构成一首门的四重奏。</p><a class="arrow-link" href="../projects/four-doors/index.html">进入四门集 <span class="arrow" aria-hidden="true">↗</span></a></figcaption></figure></main>'''
    return page('关于 monoloco — 三人艺术团体', 'monoloco，一个由三人组成的艺术团体。这里收录作品与共同的观察。', body, base, 'about')

def build():
    outputs = {'index.html': home(), 'projects/four-doors/index.html': project(), 'about/index.html': about()}
    for name, content in outputs.items():
        path = DOCS / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    # Resolve nested error URLs against the selected custom domain or project path.
    body = f'<main id="main" class="wrap error-page"><div class="eyebrow accent">404 / PAGE NOT FOUND</div><h1>走到了另一扇门。</h1><p>这个页面暂时不存在。回到作品，继续浏览。</p><a class="arrow-link" href="{BASE_PATH}index.html">返回首页 <span class="arrow" aria-hidden="true">↗</span></a></main>'
    (DOCS / '404.html').write_text(page('页面未找到 — monoloco', '回到 monoloco 作品档案。', body, BASE_PATH))
    # The preview copy is generated, never edited independently.
    preview = ROOT / 'opendesign/mockups/monoloco'
    shutil.copytree(DOCS, preview, dirs_exist_ok=True)
    sections = []
    for folder, label in [('mockups','Mockups'),('design-systems','Design Systems')]:
        groups = []
        root = ROOT / 'opendesign' / folder
        if root.exists():
            for group in sorted(root.iterdir()):
                if not group.is_dir():
                    continue
                files = sorted(group.rglob('*.html') if folder == 'mockups' else (p for p in group.rglob('*') if p.is_file()))
                if files:
                    groups.append({'slug':group.name,'files':[{'label':str(p.relative_to(group)), 'path':str(p.relative_to(ROOT/'opendesign'))} for p in files]})
        sections.append({'id':folder,'label':label,'groups':groups})
    manifest = {'generated':datetime.now(timezone.utc).isoformat(),'sections':sections}
    (ROOT / 'opendesign/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print('Built 4 static pages and refreshed OpenDesign preview.')

if __name__ == '__main__':
    build()
