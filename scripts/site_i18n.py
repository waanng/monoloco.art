"""Curated interface translations, applied while generating static English pages."""
from html.parser import HTMLParser
from html import escape
import re
COPY = {
    '/ 门之四重奏': '/ A study in doorways',
    'ABOUT MONOLOCO / 关于我们': 'ABOUT MONOLOCO',
    'MONOLOCO / 作品浏览': 'MONOLOCO / IMAGE VIEWER',
    'MONOLOCO / 艺术与生活实践': 'MONOLOCO / ART IN EVERYDAY LIFE',
    'TAKE PART / 一起动手': 'TAKE PART',
    'UPCOMING / 参与方式': 'UPCOMING / JOIN US',
    'monoloco — 艺术与生活实践': 'monoloco — Art in Everyday Life',
    'monoloco 从社区营造出发，走向策展、创作与文创设计。以影像可持续为线索，在记录与制作之间持续探索。': 'We began with community projects. Today we make photographs, drawings, exhibitions and everyday objects, finding new ways to share the things we notice.',
    'monoloco 始于 2017 年，从社区营造出发，逐渐走向策展、文创设计与持续的艺术实践。': 'Founded in 2017, monoloco is a three-person art collective. We began with community projects and now work across exhibitions and product design. We’re also developing a series of hands-on workshops.',
    'monoloco 首页': 'monoloco home',
    '← 上一组': '← Previous',
    '《杯子在溜达》· CITYWALK 速写巡展': 'A Cup on the Move · CITYWALK travelling sketch exhibition',
    '一句话，也可以是记录的开始。': 'Start with a few words.',
    '一起做些有意思的事。': 'Let’s make something together.',
    '一起创造': 'Make something together.',
    '七座城市，七段音乐记忆。': 'Seven cities, with music along the way.',
    '三个人，': 'Three people,',
    '三个人，从观察、记录到共同制作。': 'Three people. A shared curiosity. Things made together.',
    '三位成员': 'Our three members',
    '上一组': 'Previous image',
    '下一次，一起做。': 'Join us next time.',
    '下一组': 'Next image',
    '下一组 →': 'Next →',
    '不止观看，': 'Look closely.',
    '为照片留一个位置。': 'Leave a place for a photograph.',
    '主导航': 'Main navigation',
    '也亲手试试看。': 'Then try it yourself.',
    '了解工坊': 'Explore workshops',
    '交流设计合作': 'Work with us',
    '从城市速写到随身本，从校园长卷到礼品杯。让创作离开纸面，在日常物件中继续生长。': 'Urban sketches become notebooks; a painted campus panorama becomes a cup. These designs give our drawings a place in everyday life.',
    '从封面延续到腰封。': 'Wrapped for the road.',
    '从朋友的废包装纸开始，裁成小小的方形，找身边的材料做封面。带在身边，轻巧纤薄，涂涂画画，没有压力。走过的路、见过的景、探过的店、遇到的人，慢慢成为一本自己的记忆。': 'It started with wrapping paper saved by a friend: small sheets, a cover made from whatever was to hand, and a notebook light enough to carry everywhere. Fill it as you go—with sketches, photographs, tickets or a few words. Over time, the pages become a collection of places, people and things you might otherwise forget.',
    '从相机到影像。': 'From camera to image.',
    '从街区出发，': 'Rooted in the neighbourhood.',
    '从观看到动手。一起做一本本子，让光留下影子，走近胶片显影的过程。': 'Bind a notebook, make a sun print or discover how film is developed. Our workshops are a chance to try things out together.',
    '从观看，到一起动手。': 'Come and make something.',
    '从门头、土壤、城市与旅途出发，用摄影、速写和文字，留下与世界相遇的方式。': 'Doorways, gardens, familiar streets and places far from home. A collection of things we’ve noticed, photographed, drawn and written about.',
    '以手作和设计，让创作进入生活。': 'Things made by hand, and ideas made to be used.',
    '停下来，再看一眼。': 'Pause. Take another look.',
    '先做一本。': 'First, make a book.',
    '光，慢慢留下痕迹。': 'Made with sunlight.',
    '全部项目': 'All projects',
    '共同的目光': 'a shared way of seeing',
    '共同的目光。': 'a shared way of seeing.',
    '关于我们': 'About Us',
    '关于我们 — monoloco': 'About Us — monoloco',
    '关闭 ×': 'Close ×',
    '关闭大图': 'Close image viewer',
    '利物浦': 'Liverpool',
    '动手工坊': 'Hands-on Workshops',
    '动手工坊 — monoloco': 'Hands-on Workshops — monoloco',
    '可在相应平台搜索以上账号名，与我们联系。': 'Search for these account names to find us. For accounts with Chinese names, copy the name as shown.',
    '向下浏览 ↓': 'Scroll to explore ↓',
    '四门集': 'Four Doors',
    '回到 monoloco 作品与共同实践。': 'Explore monoloco’s projects, workshops and products.',
    '回到顶部 ↑': 'Back to top ↑',
    '图文整理自《忽独》第一期，影像与原文分别保留作者署名。': 'From the first issue of our magazine, Hudu (忽独). Photography and writing are credited above. Handwriting and annotations in the original artwork have been left as they are.',
    '图片暂时无法加载，请稍后重试。': 'This image could not be loaded. Please try again later.',
    '城市速写进入唱片的圆形结构，与音乐主题一起构成内页。翻过图像，空白的纸面等待新的记录。': 'Each circular insert pairs an urban sketch with the shape of a vinyl record. On the reverse, there’s room for your own notes.',
    '如何填满它？': 'What will you fill it with?',
    '如果你是文化空间、社区或活动组织者，欢迎和我们交流工坊合作。': 'Interested in hosting a workshop at your venue or as part of a community event? We’d love to hear from you.',
    '宣武门胡同 · monoloco 快闪咖啡馆': 'Xuanwumen hutong · monoloco pop-up café',
    '小红书': 'Xiaohongshu / RED',
    '小红书 · KASA': 'Xiaohongshu · KASA',
    '小红书 · 无形速写': 'Xiaohongshu · 无形速写',
    '小红书 · 瓦尔扎扎特': 'Xiaohongshu · 瓦尔扎扎特',
    '工坊内容': 'Workshop activities',
    '工坊合作与咨询': 'Host a workshop',
    '工坊正在筹备。具体时间、地点、主讲人、材料和参与方式，将在场次确定后公布。': 'We’re planning our workshops now. We’ll share dates, venues, materials and booking details as soon as each session is confirmed.',
    '巴黎': 'Paris',
    '布拉格': 'Prague',
    '影像可持续 / IMAGE': 'A LIFE BEYOND THE IMAGE / IMAGE',
    '微博': 'Weibo',
    '我们曾在胡同里做花园、办展览、记录行走，也尝试用一间快闪咖啡馆让人相遇。那些实践留下的线索，继续进入今天的作品、工坊与物件。': 'We’ve made gardens in Beijing’s hutong neighbourhoods, put on exhibitions, sketched our walks and run a pop-up café. Each was a way to bring people together. Those experiences still shape what we make today.',
    '我们用胶片、速写和手工本记录城市，也通过共同制作，让创作进入日常。影像可持续，是连接这些探索的一条线索。': 'Film, sketches and handmade notebooks help us pay attention to the places we live and visit. We’re interested in what happens next: how a photograph becomes a conversation, a drawing becomes an object, or an idea becomes something we make together.',
    '把创作的方法带到一起。做一本手工本，尝试蓝晒，走近胶片显影，让自己的日常成为作品的起点。': 'Try bookbinding, cyanotype or film developing in the company of others. There’s room to experiment, learn a new process and see where it takes you.',
    '把文字、速写和贴纸放在一起。': 'A few words, a sketch, a sticker worth keeping.',
    '把旅行路线、主题文字与唱片的视觉线索放在一起，成为一本完整的伴手本。': 'The paper wrap brings the travel routes and record-inspired graphics together, ready to take on the road.',
    '把走过的路画下来。': 'Draw a map of where you’ve been.',
    '放大观看 ↗': 'View larger ↗',
    '文创作品': 'Products',
    '文创作品 — monoloco': 'Products — monoloco',
    '曝光与水洗显影': 'Exposure and washing',
    '材料准备与涂布': 'Preparing and coating the paper',
    '柏林': 'Berlin',
    '欢迎交流工坊邀请、文化空间合作、展览与文创设计。': 'Have an idea for a workshop, exhibition or design project? We’d love to talk.',
    '浏览艺术项目': 'Explore art projects',
    '点击作品，放大观看 ↗': 'Open an image for a closer look ↗',
    '环装本': 'Ring-bound book',
    '用手绘图认识蓝晒的基本过程。实际材料与操作由现场方案和指导决定。': 'These hand-drawn guides show the basic stages: coat the paper, leave it to dry away from light, arrange the objects, expose and wash. We’ll guide you through the process during the workshop; the materials and activities will depend on the session.',
    '用摄影与速写记录观察，': 'Photographs and sketches of the world around us.',
    '白塔寺街区 · 旧物改造花园与“药局”': 'Baitasi neighbourhood · a garden made with reused objects and the “Pharmacy” project',
    '查看相关作品': 'View related projects',
    '看看旅途中的记录': 'Explore notes from our journeys',
    '看看胶片相关的城市观察': 'Explore our film photographs',
    '看见日常，': 'Find joy in the everyday.',
    '窗边，留在胶片里的光。': 'Window light, captured on film.',
    '筹备中': 'Coming soon',
    '米兰': 'Milan',
    '继续浏览艺术项目': 'Explore more art projects',
    '维也纳': 'Vienna',
    '缝线本': 'Stitched book',
    '胡同美术馆 · 插画展': 'Hutong Art Museum · illustration exhibition',
    '胶片也在我们的创作里。相机、底片和等待，让记录拥有另一种速度。': 'We use film in our own work too. With a limited number of frames and a wait before seeing the results, it asks us to slow down and look.',
    '腰封图形局部': 'Detail of the paper wrap',
    '艺术项目': 'Art Projects',
    '艺术项目 — monoloco': 'Art Projects — monoloco',
    '艺术项目、动手工坊与文创作品。monoloco 以摄影、速写、手工本和设计，记录日常并共同创造。': 'monoloco is a three-person art collective working with photography, sketching, handmade books and design. Explore our projects, workshops and products.',
    '观察 · 记录 · 制作 · 分享': 'Observe · Record · Make · Share',
    '观察，记录，留下片刻。': 'Things worth a second look.',
    '认识 LZ、KASA 和王安。monoloco 从社区营造出发，以摄影、速写、动手工坊与文创设计持续探索。': 'Meet LZ, KASA and waanng, the three people behind monoloco’s photographs, sketches, workshops and designs.',
    '认识我们': 'Meet the collective',
    '让一幅画、一段旅程，成为可以带进日常的物件。': 'Drawings and journeys, made into things to use and keep.',
    '让创作继续发生。': 'Open to what comes next.',
    '让创作，进入日常。': 'Made to be part of your day.',
    '让散页以不同的方式相连。每期工坊选取的结构与材料，将在场次中说明。': 'Stitch the pages, bind them with rings or fold them into an accordion. These original diagrams show three ways to make a book. We’ll announce the structure and materials for each workshop in advance.',
    '设计方案 / DESIGN STUDY': 'DESIGN STUDY',
    '走到了另一扇门。': 'A wrong turn, perhaps.',
    '跳到正文': 'Skip to content',
    '这个页面暂时不存在。回到作品，继续浏览。': 'We couldn’t find that page. There’s plenty to explore back in our projects.',
    '进入四门集': 'Explore Four Doors',
    '避光晾干与构图准备': 'Drying away from light and arranging the image',
    '门之四重奏': 'A study in doorways',
    '阿姆斯特丹': 'Amsterdam',
    '页脚导航': 'Footer navigation',
    '页面未找到 — monoloco': 'Page Not Found — monoloco',
    '风琴本': 'Accordion book',
    '首页': 'home',
    '上一组作品': 'Previous image',
    '下一组作品': 'Next image',
    '看看我们仨的旅途': 'Explore The Three of Us',
    '带上它，去记录。': 'Pack light. Bring a notebook.',
    '一个随身包，几支笔，一本小本子，再带上顺手的记录工具。不必准备得很复杂，出门就能把眼前的日常留下来。': 'A small bag, a few pens, a notebook and whatever else you like to use. That’s enough to get started. Take them out for a walk and see what catches your eye.',
    '包包、纸笔与随身记录工具。': 'A small kit for drawing and journalling on the go.',
    'DESIGNED OBJECTS': 'PRODUCTS',
    'DESIGNED OBJECT': 'PRODUCT DESIGN',
}
MISSING=set()
def translate(text):
    stripped=text.strip()
    if stripped in COPY:return text.replace(stripped,COPY[stripped])
    if not re.search('[\u3400-\u9fff]',stripped):return text
    if stripped in {'中文','瓦尔扎扎特','无形速写','MONOLOCO生活实验'}:return text
    for prefix,replacement in [('放大观看：','View larger: '),('查看','View '),('返回','Back to '),('筹备中 · ','Coming soon · ')]:
        if stripped.startswith(prefix):
            return text.replace(stripped,replacement+translate(stripped[len(prefix):]))
    for suffix,replacement in [('列表',' list'),('作品',' works')]:
        if stripped.endswith(suffix):return text.replace(stripped,translate(stripped[:-len(suffix)])+replacement)
    MISSING.add(stripped)
    return text
class Translator(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=False);self.result=[]
    def handle_starttag(self,tag,attrs):
        attrs=[(k,translate(v) if v is not None and k in {'alt','title','aria-label','content','data-title'} else v) for k,v in attrs]
        self.result.append('<'+tag+''.join(' '+k+(('="'+escape(v,quote=True)+'"') if v is not None else '') for k,v in attrs)+'>')
    def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs)
    def handle_endtag(self,tag):self.result.append('</'+tag+'>')
    def handle_data(self,data):self.result.append(escape(translate(data),quote=False))
    def handle_entityref(self,name):self.result.append('&'+name+';')
    def handle_charref(self,name):self.result.append('&#'+name+';')
    def handle_decl(self,decl):self.result.append('<!'+decl+'>')
    def handle_comment(self,data):self.result.append('<!--'+data+'-->')
def translate_html(content):
    parser=Translator();parser.feed(content);return ''.join(parser.result)
