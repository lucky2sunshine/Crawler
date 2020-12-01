from lxml import etree
import requests

url = 'https://bj.58.com/ershoufang/'
proxies = {
    'http':'117.69.168.203:9999',
    'http': '123.149.38.41:9999',
    'http': '123.169.117.82:9999'
    # 'http': '113.124.92.134:9999',
    # 'http': '175.42.128.165:9999',
    # 'http': '36.248.129.247:9999',
    # 'http': '110.243.21.227:9999'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
page_text = requests.get(url, proxies = proxies, headers = headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
titles = []
for li in li_list:
    title = li.xpath('./div[2]/h2/a/text()')[0]
    titles.append(title)
print(titles)
