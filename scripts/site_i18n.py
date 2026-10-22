"""Curated interface translations, applied while generating static English pages."""
from html.parser import HTMLParser
from html import escape
import re
COPY = {'/ 门之四重奏': '/ A Quartet of Doorways',
 'ABOUT MONOLOCO / 关于我们': 'ABOUT MONOLOCO',
 'MONOLOCO / 作品浏览': 'MONOLOCO / IMAGE VIEWER',
 'MONOLOCO / 艺术与生活实践': 'MONOLOCO / ART & EVERYDAY LIFE',
 'TAKE PART / 一起动手': 'TAKE PART',
 'UPCOMING / 参与方式': 'UPCOMING / JOIN US',
 'monoloco — 艺术与生活实践': 'monoloco — Art & Everyday Life',
 'monoloco 从社区营造出发，走向策展、创作与文创设计。以影像可持续为线索，在记录与制作之间持续探索。': 'From community projects to exhibitions and '
                                                          'designed objects, monoloco explores how images '
                                                          'can live on through recording, making and '
                                                          'sharing.',
 'monoloco 始于 2017 年，从社区营造出发，逐渐走向策展、文创设计与持续的艺术实践。': 'Founded in 2017, monoloco began with community projects '
                                                    'and grew into curating, object design and an ongoing '
                                                    'art practice.',
 'monoloco 首页': 'monoloco home',
 '← 上一组': '← Previous',
 '《杯子在溜达》· CITYWALK 速写巡展': 'A Cup on the Move · CITYWALK travelling sketch exhibition',
 '一句话，也可以是记录的开始。': 'A single sentence can be the start of a record.',
 '一起做些有意思的事。': 'Let’s make something together.',
 '一起创造': 'Make together',
 '七座城市，七段音乐记忆。': 'Seven cities. Seven musical memories.',
 '三个人，': 'Three people,',
 '三个人，从观察、记录到共同制作。': 'Three people. Observing, recording and making together.',
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
 '交流设计合作': 'Talk to us about a design project',
 '从城市速写到随身本，从校园长卷到礼品杯。让创作离开纸面，在日常物件中继续生长。': 'From city sketches to portable notebooks, from a campus scroll '
                                            'to a gift cup: images find new lives in objects used every day.',
 '从封面延续到腰封。': 'From the cover to the paper band.',
 '从朋友的废包装纸开始，裁成小小的方形，找身边的材料做封面。带在身边，轻巧纤薄，涂涂画画，没有压力。走过的路、见过的景、探过的店、遇到的人，慢慢成为一本自己的记忆。': 'Start with wrapping '
                                                                                      'paper saved by a '
                                                                                      'friend. Cut it down '
                                                                                      'and use materials '
                                                                                      'close at hand for a '
                                                                                      'cover. Small and '
                                                                                      'light, the notebook '
                                                                                      'goes wherever you go. '
                                                                                      'Fill it without '
                                                                                      'pressure: roads, '
                                                                                      'views, shops and '
                                                                                      'people slowly become '
                                                                                      'a memory book of your '
                                                                                      'own.',
 '从相机到影像。': 'From camera to image.',
 '从街区出发，': 'Starting in our neighbourhood,',
 '从观看到动手。一起做一本本子，让光留下影子，走近胶片显影的过程。': 'Move from looking to making. Bind a notebook, let light leave a '
                                     'silhouette, or discover how a film photograph develops.',
 '从观看，到一起动手。': 'From looking to making together.',
 '从门头、土壤、城市与旅途出发，用摄影、速写和文字，留下与世界相遇的方式。': 'Doorways, soil, cities and journeys: photographs, sketches and '
                                         'words hold our encounters with the world.',
 '以手作和设计，让创作进入生活。': 'Bring creativity into life through craft and design.',
 '停下来，再看一眼。': 'Pause. Take another look.',
 '先做一本。': 'First, make a book.',
 '光，慢慢留下痕迹。': 'Light slowly leaves its trace.',
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
 '可在相应平台搜索以上账号名，与我们联系。': 'Find us on these platforms by searching for the account names shown above. Chinese '
                         'handles are kept as written so you can find the right account.',
 '向下浏览 ↓': 'Scroll to explore ↓',
 '四门集': 'Four Doors',
 '回到 monoloco 作品与共同实践。': 'Return to monoloco’s projects and shared practice.',
 '回到顶部 ↑': 'Back to top ↑',
 '图文整理自《忽独》第一期，影像与原文分别保留作者署名。': 'Adapted from issue one of our magazine Hudu (忽独), with credit to the '
                                'original photographers and writers. Maps, handwriting and annotations in '
                                'the artworks retain their original language.',
 '图片暂时无法加载，请稍后重试。': 'This image could not be loaded. Please try again later.',
 '城市速写进入唱片的圆形结构，与音乐主题一起构成内页。翻过图像，空白的纸面等待新的记录。': 'City sketches fit inside the circle of a record, creating '
                                                'inserts that connect place and music. Turn the image over '
                                                'and a blank page awaits a new record.',
 '如何填满它？': 'What will you fill it with?',
 '如果你是文化空间、社区或活动组织者，欢迎和我们交流工坊合作。': 'If you run a cultural space, community project or event, we would love '
                                   'to discuss a workshop with you.',
 '宣武门胡同 · monoloco 快闪咖啡馆': 'Xuanwumen hutong · monoloco pop-up café',
 '小红书': 'Xiaohongshu / RED',
 '小红书 · KASA': 'Xiaohongshu · KASA',
 '小红书 · 无形速写': 'Xiaohongshu · 无形速写',
 '小红书 · 瓦尔扎扎特': 'Xiaohongshu · 瓦尔扎扎特',
 '工坊内容': 'Workshop activities',
 '工坊合作与咨询': 'Workshop enquiries & collaborations',
 '工坊正在筹备。具体时间、地点、主讲人、材料和参与方式，将在场次确定后公布。': 'Our workshops are in preparation. Dates, venues, facilitators, '
                                          'materials and booking details will be announced when each session '
                                          'is confirmed.',
 '巴黎': 'Paris',
 '布拉格': 'Prague',
 '影像可持续 / IMAGE': 'IMAGES THAT LIVE ON / IMAGE',
 '微博': 'Weibo',
 '我们曾在胡同里做花园、办展览、记录行走，也尝试用一间快闪咖啡馆让人相遇。那些实践留下的线索，继续进入今天的作品、工坊与物件。': 'We have made gardens in hutongs, '
                                                                   'organised exhibitions, recorded walks '
                                                                   'and opened a pop-up café as a place to '
                                                                   'meet. Threads from those experiences '
                                                                   'continue through today’s projects, '
                                                                   'workshops and objects.',
 '我们用胶片、速写和手工本记录城市，也通过共同制作，让创作进入日常。影像可持续，是连接这些探索的一条线索。': 'We record cities through film, sketches and '
                                                         'handmade notebooks, and bring creativity into '
                                                         'everyday life by making things together. A shared '
                                                         'question connects these explorations: how can an '
                                                         'image keep living beyond the moment it was made?',
 '把创作的方法带到一起。做一本手工本，尝试蓝晒，走近胶片显影，让自己的日常成为作品的起点。': 'Share ways of making: bind a notebook, try cyanotype or '
                                                 'explore film developing. Let everyday life become the '
                                                 'starting point for a work of your own.',
 '把文字、速写和贴纸放在一起。': 'Bring words, sketches and stickers together.',
 '把旅行路线、主题文字与唱片的视觉线索放在一起，成为一本完整的伴手本。': 'Travel routes, words and visual cues from records come together in a '
                                       'notebook made to accompany a journey.',
 '把走过的路画下来。': 'Draw the roads you have travelled.',
 '放大观看 ↗': 'View larger ↗',
 '文创作品': 'Designed Objects',
 '文创作品 — monoloco': 'Designed Objects — monoloco',
 '曝光与水洗显影': 'Exposure and washing',
 '材料准备与涂布': 'Preparing and coating the paper',
 '柏林': 'Berlin',
 '欢迎交流工坊邀请、文化空间合作、展览与文创设计。': 'Get in touch about workshops, cultural spaces, exhibitions and object design.',
 '浏览艺术项目': 'Explore art projects',
 '点击作品，放大观看 ↗': 'Select an image to view larger ↗',
 '环装本': 'Ring-bound book',
 '用手绘图认识蓝晒的基本过程。实际材料与操作由现场方案和指导决定。': 'These original hand-drawn diagrams introduce the cyanotype process. '
                                     'Materials and activities will follow each session’s plan and on-site '
                                     'guidance. The three stages below are preparing and coating, drying and '
                                     'arranging, and exposing and washing.',
 '用摄影与速写记录观察，': 'Record what we see in photographs and sketches.',
 '白塔寺街区 · 旧物改造花园与“药局”': 'Baitasi neighbourhood · a garden made with reused objects and the “Pharmacy” '
                        'project',
 '查看相关作品': 'View related projects',
 '看看旅途中的记录': 'Explore notes from our journeys',
 '看看胶片相关的城市观察': 'Explore our city photographs on film',
 '看见日常，': 'Notice the everyday.',
 '窗边，留在胶片里的光。': 'Window light held on film.',
 '筹备中': 'In preparation',
 '米兰': 'Milan',
 '继续浏览艺术项目': 'Explore more art projects',
 '维也纳': 'Vienna',
 '缝线本': 'Stitched book',
 '胡同美术馆 · 插画展': 'Hutong Art Museum · illustration exhibition',
 '胶片也在我们的创作里。相机、底片和等待，让记录拥有另一种速度。': 'Film is part of our art practice too. Cameras, negatives and the wait '
                                    'to see an image give recording a different pace.',
 '腰封图形局部': 'A detail of the paper band artwork',
 '艺术项目': 'Art Projects',
 '艺术项目 — monoloco': 'Art Projects — monoloco',
 '艺术项目、动手工坊与文创作品。monoloco 以摄影、速写、手工本和设计，记录日常并共同创造。': 'Art projects, hands-on workshops and designed objects. '
                                                     'monoloco records everyday life and makes together '
                                                     'through photography, sketching, bookbinding and '
                                                     'design.',
 '观察 · 记录 · 制作 · 分享': 'Observe · Record · Make · Share',
 '观察，记录，留下片刻。': 'Observe, record, hold a moment.',
 '认识 LZ、KASA 和王安。monoloco 从社区营造出发，以摄影、速写、动手工坊与文创设计持续探索。': 'Meet LZ, KASA and waanng. Beginning with '
                                                          'community projects, monoloco explores '
                                                          'photography, sketching, hands-on workshops and '
                                                          'object design.',
 '认识我们': 'Meet the collective',
 '让一幅画、一段旅程，成为可以带进日常的物件。': 'Let a drawing or a journey become an object you can carry into everyday life.',
 '让创作继续发生。': 'keeping creativity in motion.',
 '让创作，进入日常。': 'Bring creativity into everyday life.',
 '让散页以不同的方式相连。每期工坊选取的结构与材料，将在场次中说明。': 'Discover different ways to join loose pages. Each session will '
                                      'specify the book structure and materials used. The original diagrams '
                                      'show stitching, ring binding and accordion folding.',
 '设计方案 / DESIGN STUDY': 'DESIGN STUDY',
 '走到了另一扇门。': 'Another doorway.',
 '跳到正文': 'Skip to content',
 '这个页面暂时不存在。回到作品，继续浏览。': 'This page could not be found. Return to our projects and keep exploring.',
 '进入四门集': 'Explore Four Doors',
 '避光晾干与构图准备': 'Drying away from light and arranging the image',
 '门之四重奏': 'A Quartet of Doorways',
 '阿姆斯特丹': 'Amsterdam',
 '页脚导航': 'Footer navigation',
 '页面未找到 — monoloco': 'Page Not Found — monoloco',
 '风琴本': 'Accordion book',
 '首页': 'home',
 '上一组作品': 'Previous image',
 '下一组作品': 'Next image',
 '看看我们仨的旅途': 'Explore The Three of Us',
 '带上它，去记录。': 'Take it with you. Keep a record.',
 '一个随身包，几支笔，一本小本子，再带上顺手的记录工具。不必准备得很复杂，出门就能把眼前的日常留下来。': 'A shoulder bag, a few pens, a small notebook and the '
                                                       'tools you enjoy using. Keep it simple: take them '
                                                       'outside and start recording everyday life.',
 '包包、纸笔与随身记录工具。': 'A bag, pens, paper and portable tools for keeping a record.'}
MISSING=set()
def translate(text):
    stripped=text.strip()
    if not re.search('[\u3400-\u9fff]',stripped):return text
    if stripped in COPY:return text.replace(stripped,COPY[stripped])
    if stripped in {'中文','瓦尔扎扎特','无形速写','MONOLOCO生活实验'}:return text
    for prefix,replacement in [('放大观看：','View larger: '),('查看','View '),('返回','Back to '),('筹备中 · ','In preparation · ')]:
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
