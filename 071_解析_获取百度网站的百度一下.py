# _*_ coding : utf-8 _*_
# @Time : 2022/9/16 11:30
# @Author : xwz

# 1. 获取网页源码
# 2. xpath解析：服务器响应的数据   response.read().decode('utf-8')      etree.HTML()
# 3. 打印



# 1. 获取网页源码
import urllib.request

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 2. xpath解析：服务器响应的数据   response.read().decode('utf-8')      etree.HTML()
from lxml import etree

tree = etree.HTML(content)

result = tree.xpath('//*[@id="su"]/@value')

print(result[0])

# 3. 打印
