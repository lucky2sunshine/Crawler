# https://www.ip138.com/
# https://202020.ip138.com/

from lxml import etree
import requests
import os
import time

url = 'https://202020.ip138.com/'
proxies = {
    'https': '123.163.121.169:9999'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
page_text = requests.get(url, headers = headers, proxies = proxies ).text

tree = etree.HTML(page_text)

ip = tree.xpath('/html/body/p[1]/a/text()')[0]

print(ip)
