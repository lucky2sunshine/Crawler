# http://www.1ppt.com/moban/jianjie/

from lxml import etree
import requests
import os
import time

if not os.path.exists('./file/ppt'):
    os.mkdir('./file/ppt')

url = 'http://www.1ppt.com/moban/jianjie/'

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 一种恶心的反爬机制，服务器会验证动态生成的acw_sc_v2是否正确
    'Cookie':'acw_sc__v2=5fc640c7d47e9266a139cad624bbf863157d18bd',
    'Host': 'www.1ppt.com',
    'Referer': 'http://www.1ppt.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
}
session = requests.Session()
page_text = session.get(url, headers = headers).text
print(page_text)

tree= etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="tplist"]/li')
ppt = []
for li in li_list:
    ppt_name = li.xpath('./h2/a/text()')[0]
    ppt_name = ppt_name.encode('iso-8859-1').decode('gbk')
    ppt_url = 'http://www.1ppt.com/plus/download.php?open=0&aid=%s&cid=3' % li.xpath('./h2/a/@href')[0].split('/')[-1][:-5]
    ppt.append({'name':ppt_name, 'url':ppt_url})

# http://www.1ppt.com/plus/download.php?open=0&aid=65860&cid=3
for p in ppt:
    time.sleep(3)
    ppt_name = p.get('name')
    ppt_url = p.get('url')
    print(ppt_name, 'start download')
    download_page = requests.get(ppt_url, headers = headers).text
    download = etree.HTML(download_page)
    download_url = download.xpath('/html/body/dl/dd/ul[2]/li[1]/a/@href')[0]

    # download
    file = requests.get(download_url, headers = headers).content
    with open('./file/ppt/' + ppt_name + '.zip', 'wb') as fp:
        fp.write(file)
    print(ppt_name, 'download finish')


