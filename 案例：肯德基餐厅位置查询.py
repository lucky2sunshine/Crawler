# requests模块基本使用流程
# 1. 指定url
# 2. 发起请求
# 3. 获取响应数据
# 4. 持久化存储

import requests
import os
import json
import math

position = input('Please input position:')

totalCount = 1

def getRestPositionByPageIndex(page_index):
    global totalCount # 声明totalCount为外部的全局变量

    page_index = str(page_index)

    # 创建文件夹
    if not os.path.exists('./file'):
        os.mkdir('./file')

    # 1. 指定url、参数、请求头
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname':'',
        'pid':'',
        'keyword':position,
        'pageIndex':page_index,
        'pageSize':'10'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 2. 发起请求
    response = requests.post(url, data, headers=headers)

    # 3. 获取响应数据
    position_json = response.json()

    if page_index == '1':
        totalCount = math.ceil(position_json['Table'][0]['rowcount'] / 10)

    position_json = position_json['Table1']


    # 4. 持久化存储
    fp = open('./file/position_page'+page_index+'.json', 'w', encoding='utf-8')
    json.dump(position_json, fp, ensure_ascii=False)

    print(page_index + ' is over!')

if __name__ == '__main__':
    page_index = 1
    while page_index <= totalCount:
        getRestPositionByPageIndex(page_index)
        page_index = page_index + 1