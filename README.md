# xLog-ArticleURLCrawler

xLog-ArticleURLCrawler 是一个用于从基于 xLog 的博客中爬取文章 URL 的 Python 脚本。

本项目使用ChatGPT协助开发

## 运行流程

1. 从`config.ini`读取博客的URL
2. 通过xLog的RSS订阅功能获取文章名和文章URL
3. 多线程获取真实URL
4. 写到`article.json`

## 使用方法

1. 克隆项目到本地：
```bash
git clone https://github.com/endercatone/xLog-ArticleURLCrawler.git
```

2. 安装依赖：

```
pip install feedparser requests
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