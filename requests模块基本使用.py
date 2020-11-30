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

# 1. 指定url
url = 'https://www.sogou.com'

# 2. 发起请求
response = requests.get(url)

# 3. 获取响应数据
page_text = response.text

# 4. 持久化存储
with open('./file/sogou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

print('over!!!')