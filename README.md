# monoloco.art

monoloco 的艺术与生活实践网站。主网址：https://monoloco.art/

四个板块：**艺术项目 / 动手工坊 / 文创作品 / 关于我们**。

现有内容包括六个艺术项目、三个筹备中的工坊、两个文创设计案例和三位成员介绍，共 17 个静态页面（含首页、列表页与 404）。网页使用本地图片、字体回退和原生交互，无数据库或服务器应用。

## 本地浏览与构建

在仓库根目录运行：

~~~sh
python3 scripts/build.py
python3 scripts/check_site.py
python3 -m http.server 8289
~~~

打开 http://localhost:8289/docs/ 。构建只依赖 Python 标准库，浏览网站不依赖在线接口或外部字体。原始素材不在仓库中也可以用已提交的网页图片完成构建。

## 内容维护

- 页面文字、项目、工坊、文创及成员：scripts/site_data.py。
- 四门集清单：content/works.json。
- 提取后的图片与来源定位：content/media.json。
- 普通页面的轻量预览图清单：content/previews.json。
- 页面生成与公共布局：scripts/build.py。
- 基础样式：docs/assets/css/site.css。
- 四板块扩展样式：docs/assets/css/editorial.css。
- 大图浏览：docs/assets/js/gallery.js。

修改内容后重新构建，并运行链接检查。不要手工改生成的 HTML。构建也会刷新 opendesign/mockups/monoloco/ 预览副本与 manifest；本地预览目录不上传。

## 素材整理

原始资料位于本地 素材/ 目录，已被忽略，不上传源 PDF、演示文稿、设计源文件或参考图集。

拥有原始资料时，可安装 Pillow 和 PyMuPDF，再运行：

~~~sh
python3 scripts/prepare_assets.py
python3 scripts/extract_content_assets.py
python3 scripts/build.py
~~~

第一个脚本从 素材/12.四门集/门之四重奏.pptx 导出四门集；第二个脚本从杂志和设计资料导出精选图片及工坊手绘过程。媒体清单记录源文件、PDF 页序、图片对象或裁切区域。包装图形导出时移除红色生产辅助线。

公开图片清除 EXIF，提供 WebP 适配尺寸与 JPEG 回退。作品保留原始构图，刊物正文被重新编辑为可阅读的网页文字，未使用整刊截图代替网页。

普通页面只加载最长边 360／720px 的压缩预览图，JPEG 回退同样为小图；高像素密度屏幕也不会自动请求全尺寸图。点击放大（包括无脚本时直接打开图片）才加载原有高分辨率 JPEG。重新导出素材时会自动更新预览，也可单独运行 `python3 scripts/prepare_previews.py` 从已有网页大图生成；原有大图不会被覆盖。

## 内容状态

- 工坊均标记筹备中，不提供虚构排期、费用或报名按钮。
- 黑胶伴手本和国科大礼品杯以设计方案展示，不自动视为在售商品或实拍成品。
- 成员使用来源中的 LZ、KASA、王安；KASA 与王可的对应关系尚待确认。
- 四门集的摄影署名与具体日期仍待确认，不编造。
- 社交账号保留可搜索的原始账号名；王安英文署名为 waanng，个人 Instagram 为 @waanng。团体邮箱待申请后补充。
- “旅途中的记录”为网页编辑标题，三人团体与家庭旅行中的三个人分别表述。

详见[网站内容规划](网站内容规划.md)。原 Demo 的实现记录与版本演进见 [SPEC.md](SPEC.md)。

## 发布

GitHub Settings → Pages：

- Source：Deploy from a branch
- Branch：main
- Folder：/docs

推送 main 后由 GitHub Pages 发布。docs/CNAME 保存 monoloco.art；构建自动适配自定义域名或 GitHub 项目子路径。HTTPS 证书已批准并启用强制 HTTPS。

## 检查

~~~sh
python3 scripts/check_site.py
node --check docs/assets/js/gallery.js
~~~

另需在 375 / 768 / 1440px 浏览器检查页面、图片、大图切换、键盘方向键、Esc、首尾禁用和焦点恢复。关闭 JavaScript 后正文、列表和 JPEG 大图链接仍可用。网站不发布原始 PDF，也不含假预约、支付或账号系统。

阡陌集由 `scripts/prepare_qianmo.py` 从本地“素材/15.阡陌集”导出，收录 19 张现场记录照，原始像素尺寸为 4096px 长边。页面和列表使用轻量预览图，点击后加载大图；地点与日期不根据文件名推断。首页精选顺序为“四门集／阡陌集／五公里”。

## 中英文版本

中文网址保持原样，英文版位于 `/en/`，两种语言共用图片与样式。页首“中文 / EN”链接切换到当前页面的对应版本，并保留章节位置；浏览内部链接时保持当前语言。手写字、地图和邮戳保留作品原貌，英文图注和说明帮助阅读。不会发布原始杂志。

英文内容在 `scripts/site_data_en.py`，界面和通用文案在 `scripts/site_i18n.py`；中文内容仍在 `scripts/site_data.py` 与页面模板中。执行 `python3 scripts/build.py` 会同时生成两种语言。未收录的中文界面文字会使构建报错，避免新页面漏译。每页包含自身 canonical 以及成对的中英文 hreflang。修改图片说明时请同步更新英文 alt。
