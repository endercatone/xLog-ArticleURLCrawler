import feedparser
import requests
import json
import os
import configparser

def get_final_url(url):
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 307:
        return response.headers['Location']
    else:
        return url

def get_article_urls_from_rss(rss_url):
    feed = feedparser.parse(rss_url)

    article_urls = []
    article_count = len(feed.entries)

    for i, entry in enumerate(feed.entries, start=1):
        article_title = entry.title
        article_url = entry.link
        final_url = get_final_url(article_url)
        article_urls.append({"title": article_title, "url": final_url})

        # 打印进度
        progress = f"{i}/{article_count}"
        print(f"正在获取文章URL: {progress} - {article_title}", end='\r')

    print("获取文章URL完成！")

    return article_urls

# 读取配置文件
config = configparser.ConfigParser()
config_file = 'config.ini'

# 检查配置文件是否存在
if not os.path.exists(config_file):
    # 如果配置文件不存在，则创建一个新的配置文件并提示用户输入博客 URL
    url = input("请输入博客 URL：")

    # 创建配置文件并保存博客 URL
    config['Blog'] = {'URL': url}
    with open(config_file, 'w') as file:
        config.write(file)
else:
    # 如果配置文件存在，则读取博客 URL
    config.read(config_file)
    url = config.get('Blog', 'URL')
    print("已获取博客URL:"+url)

# 构建 RSS 请求地址
rss_url = url + "/feed?format=xml"

# 删除上一次获取后保存的 article.json 文件
if os.path.exists('article.json'):
    os.remove('article.json')

# 调用函数获取文章 URL 列表
article_urls = get_article_urls_from_rss(rss_url)

# 构造包含文章名和对应 URL 的字典列表
data = {'articles': article_urls}

# 将数据以 JSON 格式写入文件
with open('article.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)

# 获取文章数
article_count = len(article_urls)

# 输出结果
if article_count > 0:
    print("获取到的文章数：", article_count)
else:
    print("获取文章URL失败或未找到任何文章。")
