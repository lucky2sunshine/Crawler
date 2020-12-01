# http://www.1ppt.com/moban/danya/

from lxml import etree
import requests
import os
import time

if not os.path.exists('./file/ppt'):
    os.mkdir('./file/ppt')

url = 'http://www.1ppt.com/moban/danya/'

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 一种恶心的反爬机制，服务器会验证动态生成的acw_sc_v2是否正确
    'Cookie':'acw_sc__v2=5fc640c7d47e9266a139cad624bbf863157d18bd',
    #'Cookie': 'bdshare_firstime=1606822404339; UM_distinctid=1761e1421a09d9-076df10414a77a-16144b58-168000-1761e1421a15b4; __gads=ID=ffab13662c1ea475-22c9fe7cf6c400ee:T=1606822411:RT=1606822411:S=ALNI_MZmhrf6Cq4-KaDgMvVfUPwYcFG7gA; CNZZDATA5092133=cnzz_eid%3D1484824669-1606817666-%26ntime%3D1606823066; acw_tc=2760826116068243010435982e920e73f6d3e89fdcd49211d661402d744b9c; acw_sc__v2=5fc6375ab0684bbe5e83e1673c0a7ca2291426d6',
    'Host': 'www.1ppt.com',
    # If-Modified-Since: Sat, 28 Nov 2020 13:24:17 GMT
    # If-None-Match: "80d693c589c5d61:0"
    'Referer': 'http://www.1ppt.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
}
session = requests.Session()
page_text = session.get(url, headers = headers).text
# print(page_text)

tree= etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="tplist"]/li')
# print(li_list)
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


