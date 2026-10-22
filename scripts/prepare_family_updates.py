"""Export selected supplied originals, stripping metadata and retaining colour."""
from pathlib import Path
import json
from PIL import Image, ImageOps
from family_content import FAMILY_SELECTION, WORKSHOP_PHOTOS, FAMILY_ALT
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/assets/images/editorial'

def main():
    manifest=ROOT/'content/media.json'
    media=json.loads(manifest.read_text())
    selected=[(key,ROOT/'素材/工坊 - 手工本工坊'/file,zh) for key,(file,zh,en) in WORKSHOP_PHOTOS.items()]
    selected += [(key,ROOT/'素材/我们仨_原版'/file,caption) for key,file,caption,en in FAMILY_SELECTION]
    for key,source,alt in selected:
        alt=FAMILY_ALT[key][0] if key in FAMILY_ALT else alt
        with Image.open(source) as original:
            oriented=ImageOps.exif_transpose(original).convert('RGB')
            clean=Image.new('RGB',oriented.size,'white');clean.paste(oriented)
            filename=key+'.jpg'
            clean.save(OUT/filename,quality=88,optimize=True,progressive=True)
            media[key]={'image':filename,'fallback':filename,'width':clean.width,'height':clean.height,'alt':alt,'source':str(source.relative_to(ROOT)),'locator':{'file':source.name},'verification':'Selected by reviewing supplied originals. Colour and composition preserved; no date or location inferred from filenames.'}
    manifest.write_text(json.dumps(media,ensure_ascii=False,indent=2)+'\n')
    from prepare_previews import main as previews
    previews()
    print(f'Exported {len(selected)} colour originals without EXIF; 360/720px inline previews refreshed.')
if __name__=='__main__':main()
