# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 19:51
# @Author : xwz

# get请求
# 获得豆瓣电影第一页的数据 并保存

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发起请求
response = urllib.request.urlopen(request)

# 获取网站数据
content = response.read().decode("utf-8")
# print(content)

# 下载数据（写入文件）
# open方法默认情况下使用的是gbk编码      如果想要保存汉字，需要在open中制定编码格式encoding='utf8'
# 方一:
fp = open('豆瓣情色评分.json', 'w', encoding='utf8')
fp.write(content)
# 方二:
with open('豆瓣情色评分_backup.json', 'w', encoding='utf8') as fp:
    fp.write(content)
