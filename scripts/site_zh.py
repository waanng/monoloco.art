"""Chinese-only editorial labels. Brand names and original artwork text stay intact."""
from html import escape
from html.parser import HTMLParser

LABELS = {
    '01 / ART PROJECTS': '01',
    '02 / HANDS-ON WORKSHOPS': '02',
    '03 / PRODUCTS': '03',
    '04 / ABOUT US': '04',
    'ART PROJECTS': '项目目录',
    'HANDS-ON WORKSHOPS': '工坊目录',
    'PRODUCTS': '作品目录',
    'HANDS-ON WORKSHOP': '动手工坊',
    'PRODUCT DESIGN': '文创设计',
    'SELECTED PROJECT': '精选项目',
    '影像可持续 / IMAGE & EVERYDAY': '影像可持续',
    'MONOLOCO / 艺术与生活实践': '艺术与生活实践',
    'MONOLOCO / 作品浏览': '作品浏览',
    'MAKE A BOOK': '装订练习',
    'FILL IT WITH LIFE': '日常记录',
    'READY TO GO': '随身工具',
    'THE MAKING PROCESS': '制作过程',
    'OUR FILM PRACTICE': '胶片实践',
    'TAKE PART / 一起动手': '一起动手',
    'UPCOMING / 参与方式': '参与方式',
    '03 / CITIES & NOTES': '03 / 城市与音乐',
    '04 / DETAILS': '04 / 设计细节',
    '设计方案 / DESIGN STUDY': '设计方案',
    'ABOUT MONOLOCO / 关于我们': '关于我们',
    'OUR PRACTICE': '过往实践',
    "LET'S MAKE SOMETHING": '交流与合作',
    '404 / PAGE NOT FOUND': '404 / 页面未找到',
    '《杯子在溜达》· CITYWALK 速写巡展': '《杯子在溜达》· 城市漫步速写巡展',
}

def chinese_label(text):
    stripped = text.strip()
    if stripped in LABELS:
        return text.replace(stripped, LABELS[stripped])
    if stripped.startswith('ART PROJECT / '):
        text = text.replace('ART PROJECT / ', '艺术项目 / ', 1)
    return text.replace('摄影 / Photography', '摄影')

class ChinesePage(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        # Preserve URL, asset and attribute markup exactly; localise the language control's label.
        self.parts.append(self.get_starttag_text().replace('aria-label="Language"', 'aria-label="语言切换"'))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        self.parts.append(f'</{tag}>')

    def handle_data(self, data):
        self.parts.append(escape(chinese_label(data), quote=False))

    def handle_decl(self, decl):
        self.parts.append(f'<!{decl}>')

    def handle_comment(self, data):
        self.parts.append(f'<!--{data}-->')

def localize_chinese_html(content):
    parser = ChinesePage()
    parser.feed(content)
    return ''.join(parser.parts)
