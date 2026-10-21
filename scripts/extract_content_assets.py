"""Extract selected original images and design artwork; never publish source PDFs."""
from pathlib import Path
import io
import json
import xml.etree.ElementTree as ET
import fitz
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/assets/images/editorial'
SOURCE = ROOT / '素材/2023 杂志 第一期.pdf'
MEDIA = {}

def save(name, image, source, locator, alt):
    image = ImageOps.exif_transpose(image).convert('RGB')
    clean = Image.new('RGB', image.size, 'white')
    clean.paste(image)
    clean.thumbnail((1600,1600))
    clean.save(OUT / f'{name}.jpg', quality=88, optimize=True)
    large = clean.copy()
    large.save(OUT / f'{name}.webp', quality=86, method=6)
    small = clean.copy()
    small.thumbnail((640,640))
    small.save(OUT / f'{name}-small.webp', quality=83, method=6)
    MEDIA[name] = {'image':f'{name}.webp','small':f'{name}-small.webp','fallback':f'{name}.jpg',
                   'width':clean.width,'height':clean.height,'smallWidth':small.width,
                   'alt':alt,'source':str(source),'locator':locator}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    magazine=fitz.open(SOURCE)
    images = [
      ('lz',3,7,'LZ 的黑白肖像'),('kasa',18,107,'KASA 与大画幅相机的肖像'),('wangan',43,285,'王安的黑白肖像'),
      ('plant-bananas',4,12,'成串香蕉组成的黑白图案'),('plant-soil',6,20,'土壤中刚长出的幼苗'),('plant-sign',6,22,'写有禁止偷土的标识'),('plant-light',7,27,'窗边杯中的幼苗'),('plant-pigs',8,36,'栏杆后的小猪'),('plant-detail',9,42,'细网与植物的局部'),
      ('travel-window',12,63,'旅行途中，脚下向外展开的远景'),('travel-street',13,68,'街口的人群与经过的车辆'),('travel-shop',13,70,'店面前的人和门口的陈设'),('travel-cat',14,77,'窗边看向镜头的猫'),('travel-water',15,81,'水面的涟漪与一只水鸟'),('travel-lane',15,83,'狭窄巷道中悬挂的标识'),('travel-station',16,88,'站台与铁轨旁的列车'),('travel-bridge',16,90,'走过木质通道的人'),
      ('five-city',20,114,'高处望去的城市屋顶与天际线'),('five-window',21,118,'胶片记录的窗边书本与光影'),('five-reader',21,120,'窗前阅读的人'),('five-portrait',22,137,'读书的人与书页的细节'),('five-building',22,139,'明亮天井与环绕的建筑走廊'),('five-door',23,144,'标有 D-22 的入口'),('five-branches',24,150,'窗外伸展的树枝'),('five-library',26,171,'阅览室的灯光与桌椅'),('five-seat',27,180,'坐在窗边的人与光影'),('five-studio',30,211,'堆放画作与书本的室内空间'),('five-room',31,220,'有植物、绘画和家具的房间'),
      ('film-camera',42,278,'玛米亚 C220 双镜头相机的手绘结构图'),
      ('journey-map',45,298,'手绘旅途路线图'),('journey-list',45,300,'旅程中到访地点的手写清单'),('journey-road',46,305,'在建筑前走过的一大一小两个身影'),('journey-trees',46,307,'树下的步道与向前延伸的路'),('journey-texas',47,313,'用文字和路线记录德州的手绘地图'),('journey-family',48,319,'旅途中一家人在门前的合影'),('journey-west',49,325,'一号公路旅程的手绘路线与地点'),('journey-house',50,331,'旅途中路过的街角房子'),('journey-east',51,339,'美国东部旅途的手绘路线'),('journey-campus',52,347,'登上校园台阶的孩子'),('journey-bookshop',54,366,'一家书店门前的旅行记录'),('journey-balloon',55,377,'街边与气球合影的家人'),
      ('notebooks',56,385,'九本由不同封面与装订方式制作的随身小本'),('notebook-map',58,427,'手工本中绘制的路线地图'),('notebook-writing',59,455,'小本子上的手写记录'),('notebook-coffee',59,457,'手工本中收集的文字、速写与贴纸'),('notebook-photo',59,463,'本子中粘贴的两张照片')
    ]
    for name,page,xref,alt in images:
        pix=fitz.Pixmap(magazine,xref)
        if pix.n>4: pix=fitz.Pixmap(fitz.csRGB,pix)
        image=Image.open(io.BytesIO(pix.tobytes('png')))
        if image.mode=='RGBA':
            bg=Image.new('RGBA',image.size,'white');bg.alpha_composite(image);image=bg.convert('RGB')
        save(name,image,'素材/2023 杂志 第一期.pdf',{'page':page,'xref':xref},alt)
    book='素材/文创 - 黑胶伴手本/黑胶书店伴手礼本设计-深烘咖啡版.pdf'
    doc=fitz.open(ROOT/book)
    entries=[('vinyl-cover',1,(160,60,820,480),'黑胶伴手本封面设计：唱机图形与 BEYOND THE NOTES 字样'),('vinyl-label',3,(175,55,810,460),'借用唱片内环形式的姓名与使用日期扉页')]
    for i,city in enumerate(['利物浦','阿姆斯特丹','柏林','布拉格','维也纳','米兰','巴黎'],5):
        entries.append((f'vinyl-city-{i-4}',i,(180,60,485,447),city+'城市速写与唱片造型内页设计'))
    entries.append(('vinyl-band',13,(280,166,815,279),'腰封局部：旅行路线与跟着黑胶去旅行字样'))
    for name,n,rect,alt in entries:
        pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(rect),alpha=False)
        save(name,Image.frombytes('RGB',(pix.width,pix.height),pix.samples),book,{'page':n,'clip':rect},alt)
    cup='素材/文创 - 国科大礼品杯/国科大礼品咖啡杯设计.pdf'
    doc=fitz.open(ROOT/cup)
    for name,n,rect,alt in [
       ('ucas-scroll',1,(32,270,925,440),'以校园建筑和题字组成的彩色校园长卷'),
       ('ucas-sketch',2,(66,290,900,475),'四组校园建筑的手绘线稿'),
       ('ucas-package',3,(140,190,805,415),'以校园建筑几何图形组成的包装设计局部'),
       ('ucas-cup',4,(170,100,880,525),'国科大礼品杯正反面图案的平面设计方案')]:
        source_page=doc[n-1]
        clean_svg=None
        if name=='ucas-package':
            # Production cutting/folding paths are a separate red vector layer.
            # Remove that layer from the source vector artwork before rendering.
            svg=ET.fromstring(source_page.get_svg_image())
            for parent in svg.iter():
                for child in list(parent):
                    if child.get('stroke','').lower()=='#e60013':
                        parent.remove(child)
            clean_svg=fitz.open(stream=ET.tostring(svg),filetype='svg')
            source_page=clean_svg[0]
        pix=source_page.get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(rect),alpha=False)
        save(name,Image.frombytes('RGB',(pix.width,pix.height),pix.samples),cup,{'page':n,'clip':rect,'productionLinesRemoved':name=='ucas-package'},alt)
    for name,path,alt in [
       ('cyanotype-process','素材/工坊 - 蓝晒工坊/蓝晒手绘说明.png','从涂布到曝光、水洗的蓝晒手绘过程说明'),
       ('cyanotype-print','素材/工坊 - 蓝晒工坊/蓝晒.png','蓝晒过程中植物影像从纸面显现的过程图'),
       ('binding-process','素材/工坊 - 手工本工坊/手工书工坊说明.png','缝线本、环装本、风琴本与照片、文字、印章的手绘说明')]:
        im=Image.open(ROOT/path)
        # Export instructions in individual readable steps, avoiding very long images.
        parts=3 if name in ['binding-process','cyanotype-process'] else 1
        if name=='binding-process':
            bounds=[920,3090,4940,6540]
        elif name=='cyanotype-process':
            bounds=[0,960,2030,3240]
        else:
            bounds=[0,im.height]
        for part in range(parts):
            crop=im.crop((0,bounds[part],im.width,bounds[part+1]))
            save(f'{name}-{part+1}',crop,path,{'segment':part+1,'total':parts},alt+f'，第 {part+1} 部分')
    (ROOT/'content/media.json').write_text(json.dumps(MEDIA,ensure_ascii=False,indent=2)+'\n')
    from prepare_previews import main as prepare_previews
    prepare_previews()
    print(f'Exported {len(MEDIA)} assets with source provenance.')

if __name__=='__main__':main()
