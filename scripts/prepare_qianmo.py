"""Export Qianmo field-record photographs, keeping originals untouched."""
from pathlib import Path
import json
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '素材/15.阡陌集'
OUT = ROOT / 'docs/assets/images/editorial'

def main(generate_previews=True):
    path = ROOT / 'content/media.json'
    media = json.loads(path.read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(SOURCE.glob('*.jpg'))
    if not files:
        raise FileNotFoundError(f'No source images in {SOURCE}')
    for i, source in enumerate(files, 1):
        key = f'qianmo-{i:02d}'
        with Image.open(source) as original:
            oriented = ImageOps.exif_transpose(original).convert('RGB')
            clean = Image.new('RGB', oriented.size, 'white')
            clean.paste(oriented)
            filename = f'{key}.jpg'
            clean.save(OUT / filename, quality=88, optimize=True, progressive=True)
            media[key] = {
                'image':filename, 'fallback':filename,
                'width':clean.width, 'height':clean.height,
                'alt':f'阡陌集现场记录 {i:02d}：展开的旅行画册与现场风景，画页上保留速写、地图或邮票邮戳等记录。',
                'source':str(source.relative_to(ROOT)),
                'locator':{'file':source.name},
                'verification':'Project meaning and authorship supplied by the artist; no location or date inferred from filenames.'
            }
    path.write_text(json.dumps(media,ensure_ascii=False,indent=2)+'\n')
    if generate_previews:
        from prepare_previews import main as prepare_previews
        prepare_previews()
    print(f'Exported {len(files)} Qianmo photographs at original pixel dimensions; EXIF removed.')

if __name__ == '__main__':
    main()
