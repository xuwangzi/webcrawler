# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 10:45
# @Author : xwz

import urllib.request

url = 'https://www.baidu.com'

# url的组成
"""
    协议：http/https
    主机：www.baidu.com
    端口号：
        http    80
        https   443
        mysql   3306
        oracle  1521
        redis   6379
        mongodb 27017
    路径
    参数
    锚点
    
    https://www.baidu.com/baidu?tn=monline_4_dg&ie=utf-8&wd=oracle
    协议      主机地址      路径    参数              参数    参数        锚点（#）
"""

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)
# 遇到了 UA反扒(User Agent)

print('===============遇到了UA反扒(User Agent)↑=======================================================')

print('===============请求对象的定制↓==================================================================')

# 我的header里的UA：
# User-Agent
# 	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}

# 因为urlopen方法不能存储字典，所以headers不能传入
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)


