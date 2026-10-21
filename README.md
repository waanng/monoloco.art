# monoloco.art

monoloco 三人艺术团体的摄影书风格网站 Demo。首个项目“四门集 / 门之四重奏”收录 12 组四联作品。

主域名：https://monoloco.art/ （需完成域名 DNS 解析与 HTTPS 证书签发）。

## 本地浏览

在仓库根目录运行：

```sh
python3 -m http.server 8289
```

打开 http://localhost:8289/docs/ 。首页、作品页、关于页为静态 HTML，不依赖在线接口或外部字体。

## 更新作品

1. 在 `content/works.json` 更新图片清单、地点与替代文本。
2. 将处理好的图片放入 `docs/assets/images/four-doors/`。每组提供 JPEG 回退，以及 640px / 1080px WebP；保留四联构图，不放大超出原始分辨率。
3. 运行 `python3 scripts/build.py` 重新生成页面。
4. 运行 `python3 scripts/check_site.py` 检查链接与资源。
5. 提交并推送到 main；Pages 从 `/docs` 发布。

项目页选集数量由清单自动计算。生成页面的正文在 `scripts/build.py`，样式在 `docs/assets/css/site.css`，大图交互在 `docs/assets/js/gallery.js`。

`scripts/build.py` 只使用 Python 标准库。它也会生成本地 `opendesign/mockups/monoloco/` 预览副本和 manifest；该目录不上传。

## 素材来源

初始图片从本地 `12.四门集/门之四重奏.pptx` 的相应页面直接提取，地点与图片对应关系记录在 `content/works.json`。

有原始资料时，可安装 Pillow 后运行 `python3 scripts/prepare_assets.py` 重新导出。原始资料不上传公开仓库；没有原始资料也可以使用已提交的网页图片重新生成全部页面。

作品日期和作者署名未确认，公开页面不展示。三位成员姓名、个人履历和联系信息尚未提供，关于页仅展示已知团体信息。中英项目短语为本 Demo 的界面译文，不是作者确认的正式英文作品名。

作品图片不附加开放使用许可；网站可公开浏览不等于图片获得再使用授权。

## 发布设置

GitHub → Settings → Pages：

- Source：Deploy from a branch
- Branch：main
- Folder：/docs

`.nojekyll` 保证直接发布静态文件。所有普通页面使用相对路径，构建脚本根据 docs/CNAME 自动决定 404 基路径和分享图的域名。修改域名后重新构建即可。

GitHub Pages 已设置自定义域名 monoloco.art，并保存于 docs/CNAME。DNSPod 中根域名 @ 应添加四条 A 记录：185.199.108.153、185.199.109.153、185.199.110.153、185.199.111.153；www 的 CNAME 指向 waanng.github.io。DNS 检查通过、证书可用后启用 Enforce HTTPS。

## 检查

- `python3 scripts/build.py`
- `python3 scripts/check_site.py`
- `node --check docs/assets/js/gallery.js`
- 在 375 / 768 / 1440px 浏览器中检查页面溢出、图片加载及大图上一组、下一组、首尾禁用、键盘箭头、Esc 和焦点恢复。
- 关闭 JavaScript 时作品列表、正文和 JPEG 大图链接仍可用。

不要手工编辑生成的 `index.html`；修改生成脚本后重新构建，以保持内容一致。

设计规格见 [SPEC.md](SPEC.md)。本项目不含服务器、联系表单或账号系统。
