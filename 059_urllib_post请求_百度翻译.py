# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 12:00
# @Author : xwz

import urllib.request
import urllib.parse

# 找到对应的接口
url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post请求的参数 必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
# post请求的参数 不是拼接在url之后，需要放在请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发起请求
response = urllib.request.urlopen(request)

# 获取网站数据
content = response.read().decode("utf-8")

# 打印
print(type(content))
print(content)


# str字符串 => json对象
import json

obj = json.loads(content)
print(type(obj))
print(obj)



