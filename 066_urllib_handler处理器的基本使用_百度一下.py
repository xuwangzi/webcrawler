# _*_ coding : utf-8 _*_
# @Time : 2022/9/15 15:38
# @Author : xwz



import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
}

request = urllib.request.Request(url=url, headers=headers)

# 1. 获取handler对象
handler = urllib.request.HTTPHandler()
# 2. 获取opener对象
opener = urllib.request.build_opener(handler)
# 3. 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
