# requests模块基本使用流程
# 1. 指定url
# 2. 发起请求
# 3. 获取响应数据
# 4. 持久化存储

import requests
import os
import json

def getMovieByPageIndex(page_index):
    # 创建文件夹
    if not os.path.exists('./file'):
        os.mkdir('./file')

    # 1. 指定url、参数、请求头
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type':'25',
        'interval_id':'100:90',
        'action':'',
        'start':str(page_index*20),
        'limit':'20'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 2. 发起请求
    response = requests.get(url, param, headers=headers)

    # 3. 获取响应数据
    movie_json = response.json()

    # 4. 持久化存储
    fp = open('./file/movie'+str(page_index)+'.json', 'w', encoding='utf-8')
    json.dump(movie_json, fp, ensure_ascii=False)

    print(str(page_index) + ' is over!')

if __name__ == '__main__':
    for i in range(0,10):
        getMovieByPageIndex(i)