# xLog-ArticleURLCrawler

xLog-ArticleURLCrawler 是一个用于从基于 xLog 的博客中爬取文章 URL 的 Python 脚本。

## 功能特点

- 通过提供的 RSS 订阅 URL，从博客中获取文章 URL。
- 支持处理跳转链接，获取最终的文章 URL。
- 输出文章标题和对应的 URL。
- 将获取到的文章 URL 保存为 JSON 文件。

## 使用方法

1. 克隆项目到本地：
```bash
git clone https://github.com/endercatone/xLog-ArticleURLCrawler.git
```

2. 安装依赖：

```
pip install feedparser requests tqdm
```

3. 在终端中运行脚本：

```bash
python main.py
```

4. 根据提示输入博客的 URL，例如：

```
博客URL: https://example.com
```

5. 等待脚本执行完成。获取到的文章 URL 将保存在当前目录下的 `article.json` 文件中。

6. 打开 `article.json` 文件，即可查看获取到的文章标题和对应的 URL。

## 许可证

该项目使用 MIT 许可证。详细信息请参阅 LICENSE 文件。