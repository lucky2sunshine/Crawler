# 爬取太快会被封IP

from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 获取目录所在网页源码
response = requests.get(url, headers = headers)
page_text = response.text
# 解析目录所在网页源码
soup = BeautifulSoup(page_text, 'lxml')
# 获取目录
contents = soup.select('.book-mulu > ul > li > a')
# 存储整本书
articles = []
# 遍历目录
for content in contents:
    time.sleep(4)
    # 章节名
    content_name = content.string
    # 章节URL
    content_url = content['href']
    # 解析章节
    paragraphs = BeautifulSoup(requests.get('https://www.shicimingju.com' + content_url).text, 'lxml').select('.chapter_content > p')
    # 添加章节名
    articles.append(content_name)
    print('解析',content_name)
    # 遍历每一段，将每一段加入articles
    for paragraph in paragraphs:
        articles.append(paragraph.string)
# 存储
with open('./file/sanguoyanyi.txt', 'w+', encoding='utf-8') as fp:
    for article in articles:
        fp.write(article)
        fp.write('\n')
    print('over!')