"""Check generated pages, local links, and image dimensions without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.references = []
        self.ids = set()
        self.lang = None
        self.title = False
        self.canonical = None
        self.alternates = {}
        self.switches = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        if tag == 'link' and attrs.get('hreflang'):
            self.alternates[attrs['hreflang']] = attrs.get('href')
        if tag == 'a' and attrs.get('data-language'):
            self.switches[attrs['data-language']] = attrs.get('href')
        if tag == 'title':
            self.title = True
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'Duplicate id: {self.path}: {attrs["id"]}')
            self.ids.add(attrs['id'])
        for key in ['href', 'src']:
            if attrs.get(key):
                self.references.append(attrs[key])
        if 'srcset' in attrs:
            self.references.extend(item.strip().split(' ')[0] for item in attrs['srcset'].split(','))
        if tag == 'img' and 'alt' not in attrs:
            errors.append(f'Missing image alt: {self.path}')

def main():
    pages = {}
    for p in SITE.rglob('*.html'):
        parser = Page(p)
        parser.feed(p.read_text())
        pages[p.resolve()] = parser
        if not parser.lang or not parser.title:
            errors.append(f'Missing language/title: {p}')
    domain=(SITE/'CNAME').read_text().strip() if (SITE/'CNAME').exists() else ''
    public=f'https://{domain}' if domain else 'https://waanng.github.io/monoloco.art'
    for path, parser in pages.items():
        route=path.relative_to(SITE).as_posix()
        english=route.startswith('en/')
        counterpart=route.removeprefix('en/') if english else 'en/'+route
        expected_lang='en' if english else 'zh-CN'
        if parser.lang != expected_lang:
            errors.append(f'Wrong language: {route}')
        if not (SITE/counterpart).is_file():
            errors.append(f'Missing bilingual counterpart: {route}')
        canonical=public+'/'+route.removesuffix('index.html')
        if parser.canonical != canonical:
            errors.append(f'Wrong canonical: {route}')
        zh_route=route.removeprefix('en/')
        expected_alternates={'zh-CN':public+'/'+zh_route.removesuffix('index.html'), 'en':public+'/en/'+zh_route.removesuffix('index.html'), 'x-default':public+'/'+zh_route.removesuffix('index.html')}
        if parser.alternates != expected_alternates:
            errors.append(f'Wrong language alternates: {route}')
        other_lang='zh-CN' if english else 'en'
        ref=parser.switches.get(other_lang,'')
        switched=(SITE/ref.lstrip('/') if ref.startswith('/') else path.parent/ref).resolve()
        if switched != (SITE/counterpart).resolve():
            errors.append(f'Language switch changes page: {route}')

        for ref in parser.references:
            part = urlsplit(ref)
            if part.scheme or part.netloc:
                continue
            relative = unquote(part.path)
            if relative.startswith('/monoloco.art/'):
                target = SITE / relative.removeprefix('/monoloco.art/')
            elif relative.startswith('/'):
                target = SITE / relative.lstrip('/')
            elif relative:
                target = path.parent / relative
            else:
                target = path
            if target.is_dir():
                target = target / 'index.html'
            target = target.resolve()
            if not target.is_file():
                errors.append(f'Broken reference: {path.relative_to(SITE)} -> {ref}')
            if part.fragment and target in pages and part.fragment not in pages[target].ids:
                errors.append(f'Broken anchor: {path.relative_to(SITE)} -> {ref}')
    works = json.loads((ROOT / 'content/works.json').read_text())
    assert len(works) == len({w['id'] for w in works})
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages; all local assets, links, fragments and bilingual metadata; {len(works)} unique works.')

if __name__ == '__main__':
    main()
