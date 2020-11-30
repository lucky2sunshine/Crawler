# requests模块基本使用流程
# 1. 指定url
# 2. 发起请求
# 3. 获取响应数据
# 4. 持久化存储

import requests
import os
# 创建文件夹
if not os.path.exists('./file'):
    os.mkdir('./file')

# 1. 指定url、参数、请求头
url = 'https://www.baidu.com/s'
wd = input('Please input a word:')
param = {
    'wd':wd
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 2. 发起请求
response = requests.get(url, param, headers=headers)

# 3. 获取响应数据
page_text = response.text

# 4. 持久化存储
with open('./file/'+wd+'.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

print('over!!!')