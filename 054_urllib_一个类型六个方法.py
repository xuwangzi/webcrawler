# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 9:52
# @Author : xwz

import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# response是HTTPResponse类型
# <class 'http.client.HTTPResponse'>
# print(type(response))

# 一字节一字节的读
# content = response.read()
# print(content)
# 返回5个字节
# content = response.read(5)
# print(content)
# 读取一行
# content = response.readline()
# print(content)
# 一行一行的读
# content = response.readlines()
# print(content)

# 返回状态码
# 200 没问题
print(response.getcode())

# 返回url
print(response.geturl())

# 获取状态信息
print(response.getheaders())
