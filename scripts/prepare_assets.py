"""Export selected four-panel photographs from the local source presentation.

Requires Pillow; run from any directory. Original presentation is never changed.
"""
from pathlib import Path
from PIL import Image, ImageOps
import io
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '素材' / '12.四门集' / '门之四重奏.pptx'
OUT = ROOT / 'docs/assets/images/four-doors'
SELECTION = [
    (25, 30, '波士顿牛津街', '四幅门头并置：砖墙、深色木门与石砌入口。'),
    (9, 14, '斯坦福大学', '四幅门头并置：木门、雕花石墙与拱形入口。'),
    (34, 38, '广州 289 艺术区', '四幅门头并置：玻璃店面、绿色植物与不同尺度的入口。'),
    (13, 18, '莱斯大学', '四幅门头并置：浅色拱廊、门前台阶与棕色木门。'),
    (15, 20, '华盛顿大学', '四幅门头并置：石砌立面、拱门与有雕饰的建筑入口。'),
    (21, 26, '犹他大学', '四幅门头并置：石柱、木门与玻璃入口。'),
    (24, 29, '波士顿自由之路', '四幅门头并置：红色砖墙与色彩各异的商店入口。'),
    (31, 35, '宾州大学', '四幅门头并置：砖石拱门、门前台阶与深色双扇门。'),
    (11, 16, 'SMU', '四幅门头并置：红砖、白色门框、绿植与庭院入口。'),
    (14, 19, 'Baylor 大学', '四幅门头并置：砖砌立面、浅色门框与门前阶梯。'),
    (36, 40, '浙江大学之江学院', '四幅门头并置，记录同一地点不同建筑入口的形态。'),
    (37, 41, '中国美术学院象山校区', '四幅门头并置，记录校园建筑中不同的门与入口。'),
]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    works = []
    with zipfile.ZipFile(SOURCE) as archive:
        for order, (page, media, title, alt) in enumerate(SELECTION, 1):
            slug = f'doors-{order:02d}'
            source_image = f'ppt/media/image{media}.jpg'
            image = ImageOps.exif_transpose(Image.open(io.BytesIO(archive.read(source_image)))).convert('RGB')
            # New image removes source metadata from public derivatives.
            clean = Image.new('RGB', image.size)
            clean.paste(image)
            clean.save(OUT / f'{slug}.jpg', quality=90, optimize=True)
            for size, suffix in [(640, 'small'), (1080, 'large')]:
                variant = clean.copy()
                variant.thumbnail((size, size))
                variant.save(OUT / f'{slug}-{suffix}.webp', quality=86, method=6)
            works.append({
                'id': slug, 'order': order, 'titleZh': title,
                'sourceFile': '素材/12.四门集/门之四重奏.pptx',
                'sourcePage': page, 'sourceImage': source_image,
                'location': title, 'displayDate': None, 'credit': None,
                'image': f'{slug}-large.webp', 'thumbnail': f'{slug}-small.webp',
                'fallback': f'{slug}.jpg', 'width': clean.width, 'height': clean.height,
                'altZh': alt,
                'verification': 'Image and location paired directly from source slide. Dates and authorship omitted pending confirmation.'
            })
    path = ROOT / 'content/works.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(works, ensure_ascii=False, indent=2) + '\n')
    from prepare_previews import main as prepare_previews
    prepare_previews()
    print(f'Exported {len(works)} works.')

if __name__ == '__main__':
    main()
