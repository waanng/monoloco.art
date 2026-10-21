"""Make lightweight inline previews; keep full-size gallery files unchanged."""
from pathlib import Path
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'

def main():
    previews = {}
    for manifest, group, id_field in [('media.json','editorial',None),('works.json','four-doors','id')]:
        source = json.loads((ROOT / 'content' / manifest).read_text())
        items = [(w[id_field],w) for w in source] if id_field else source.items()
        folder = SITE / 'assets/images' / group
        for key, item in items:
            with Image.open(folder / item['fallback']) as original:
                original = original.convert('RGB')
                variants = []
                for edge, quality in [(360,60),(720,68)]:
                    image = original.copy()
                    image.thumbnail((edge,edge),Image.Resampling.LANCZOS)
                    filename = f'{key}-preview-{edge}.webp'
                    image.save(folder / filename,quality=quality,method=6)
                    if not variants or image.width != variants[-1]['width']:
                        variants.append({'file':filename,'width':image.width,'height':image.height})
                fallback = original.copy()
                fallback.thumbnail((720,720),Image.Resampling.LANCZOS)
                filename = f'{key}-preview.jpg'
                fallback.save(folder / filename,quality=70,optimize=True,progressive=True)
                previews[f'{group}/{key}'] = {'sources':variants,'fallback':filename}
    (ROOT / 'content/previews.json').write_text(json.dumps(previews,ensure_ascii=False,indent=2)+'\n')
    print(f'Prepared lightweight previews for {len(previews)} images; gallery originals unchanged.')

if __name__ == '__main__':
    main()
