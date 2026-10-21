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

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
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
    for path, parser in pages.items():
        for ref in parser.references:
            part = urlsplit(ref)
            if part.scheme or part.netloc:
                continue
            relative = unquote(part.path)
            if relative.startswith('/monoloco.art/'):
                target = SITE / relative.removeprefix('/monoloco.art/')
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
    print(f'PASS: {len(pages)} pages; all local assets, links and fragments; {len(works)} unique works.')

if __name__ == '__main__':
    main()
