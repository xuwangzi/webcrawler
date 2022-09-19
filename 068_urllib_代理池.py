# _*_ coding : utf-8 _*_
# @Time : 2022/9/15 16:30
# @Author : xwz


import random
import urllib.request

# 代理池（国内普通代理）
proxies_pool = [
    {'http': '218.7.171.91:3128'},
    {'http': '47.92.113.71:80'},
]

proxies = random.choice(proxies_pool)
print(proxies)

url = 'http://www.ip111.cn/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 1. 获取handler对象
handler = urllib.request.ProxyHandler(proxies = proxies)
# 2. 获取opener对象
opener = urllib.request.build_opener(handler)
# 3. 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip结果页面_随机代理池.html', 'w', encoding='utf-8')as fp:
    fp.write(content)





