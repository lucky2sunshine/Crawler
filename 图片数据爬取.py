# <img src="https://fanyiapp.cdn.bcebos.com/cms/image/7d006fe094f4910322c379814ece6d9d.jpg">

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
url = 'https://fanyiapp.cdn.bcebos.com/cms/image/7d006fe094f4910322c379814ece6d9d.jpg'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 2. 发起请求
response = requests.get(url, headers=headers)

# 3. 获取响应数据
img_data_binary = response.content

# 4. 持久化存储
with open('./file/' + url.split('/')[-1],'wb') as fp:
    fp.write(img_data_binary)

print('over!!!')