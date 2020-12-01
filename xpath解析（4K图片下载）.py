from lxml import etree
import requests
import os
import time

if not os.path.exists('./file/imgs'):
    os.mkdir('./file/imgs')

url = 'http://pic.netbian.com/4kmeinv/'
proxies = {
    'http': '123.149.38.41:9999',
    'http': '123.169.117.82:9999',
    'http': '113.124.92.134:9999',
    'http': '175.42.128.165:9999',
    'http': '36.248.129.247:9999',
    'http': '110.243.21.227:9999'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
page_text = requests.get(url, headers = headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="clearfix"]/li')
for li in li_list:
    time.sleep(2)
    img_url = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0]
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    img_data = requests.get(img_url, headers = headers).content
    with open('./file/imgs/' + img_name + '.jpg', 'wb') as fp:
        fp.write(img_data)
    print(img_name + ' is finish')
print('Task is finish!')