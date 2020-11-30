# requests模块基本使用流程
# 1. 指定url
# 2. 发起请求
# 3. 获取响应数据
# 4. 持久化存储

import requests
import os
import json
# 创建文件夹
if not os.path.exists('./file'):
    os.mkdir('./file')

# 1. 指定url、参数、请求头
url = 'https://fanyi.baidu.com/sug'
kw = input('Please input a word:')
data = {
    'kw':kw
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 2. 发起请求
response = requests.post(url, data, headers=headers)

# 3. 获取响应数据
kw_json = response.json()

# 4. 持久化存储
json.dump(kw_json, open('./file/'+kw+'.json','w',encoding='utf-8'),ensure_ascii=False)

print('over!!!')