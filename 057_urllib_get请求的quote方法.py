# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 11:21
# @Author : xwz

import urllib.request

# 获取周杰伦的网页源码
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&fenlei=256&rsv_pq=92df06730000c29e&rsv_t=b95aIkggAjFq3loz4zkoL3aj6q2cf3p3e8Hwpwvm4zVzDiioNv5fsrAD04km&rqlang=en&rsv_dl=tb&rsv_enter=1&rsv_sug3=10&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6&rsp=5&inputT=1539&rsv_sug4=2152
# 周杰伦变成了乱码
url = 'https://www.baidu.com/s?wd='

# 将“周杰伦”变成unicode编码格式
name = urllib.parse.quote('周杰伦')
print(name)
url += name


# 请求对象定制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)



