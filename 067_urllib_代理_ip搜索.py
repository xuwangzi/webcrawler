# _*_ coding : utf-8 _*_
# @Time : 2022/9/15 15:49
# @Author : xwz


import urllib.request

url = 'http://www.ip111.cn/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 代理：黑龙江省绥化市 联通（普通代理）
proxies = {
    'http':'218.7.171.91:3128'
}
# 1. 获取handler对象
handler = urllib.request.ProxyHandler(proxies = proxies)
# 2. 获取opener对象
opener = urllib.request.build_opener(handler)
# 3. 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip结果页面.html', 'w', encoding='utf-8')as fp:
    fp.write(content)

