# https://www.aqistudy.cn/historydata/

from lxml import etree
import requests
import os
import time

url = 'https://www.aqistudy.cn/historydata/'
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

# 不同表达式之间使用 ｜ 隔开
citys = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li/a/text() | /html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]//a/text()')

print(len(citys),citys)
