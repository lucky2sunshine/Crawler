# https://www.qiushibaike.com/imgrank/page/1/

# 数据解析基本使用流程
# 1. 指定url
# 2. 发起请求
# 3. 获取响应数据
# 4. 数据解析
# 5. 持久化存储

import requests
import os
import re

def getImgByUrl(url):
    # 创建文件夹
    if not os.path.exists('./file'):
        os.mkdir('./file')

    # 1. 指定url、参数、请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 2. 发起请求
    response = requests.get(url, headers=headers)

    # 3. 获取响应数据
    img_data_binary = response.content

    # 4. 持久化存储
    with open('./file/' + url.split('/')[-1], 'wb') as fp:
        fp.write(img_data_binary)

    print(url.split('/')[-1] + ' is over!')

def getImgByPageIndex(page_index):

    # 创建文件夹
    if not os.path.exists('./file'):
        os.mkdir('./file')

    # 1. 指定url、参数、请求头
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    url = url%page_index

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 2. 发起请求
    response = requests.get(url, headers=headers)

    # 3. 获取响应数据
    page_text = response.text

    # 4. 数据解析
    regex = '<div class="thumb">.*?<img src="([/\w\.]*)".*?</div>'
    img_src_list = re.findall(regex, page_text,re.S)
    # 加上请求头
    img_src_list = ['https:'+src for src in img_src_list]

    # 5. 持久化存储
    for url in img_src_list:
        getImgByUrl(url)

if __name__ == '__main__':
    for i in range(1, 5):
        getImgByPageIndex(i)