# _*_ coding : utf-8 _*_
# @Time : 2022/9/15 9:35
# @Author : xwz


import urllib.request
import urllib.error

url = 'https://blog.csdn.net/QQ1528884535/article/details/109281630'

# url = 'https://blog.csdn.net/QQ1528884535/article/details/1092816301'
# url = 'https://blog.csdn345.net/QQ1528884535/article/details/109281630'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级。。。（doge')
except urllib.error.URLError:
    print('哎呀，都说了。系统正在升级。。。（恼')



