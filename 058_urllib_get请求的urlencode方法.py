# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 11:39
# @Author : xwz



import urllib.parse
import urllib.request

# urlencode应用场景：多参数编码
# https://www.baidu.com/s?wd=周杰伦&sex=男

url_base = 'https://www.baidu.com/s?'

data = {
    'wd': '蔡徐坤',
    'sex': '男',
    'hobby': '唱跳rap'
}
url_attach = urllib.parse.urlencode(data)

# 请求资源路径
url = url_base + url_attach

# 请求对象定制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发起请求
response = urllib.request.urlopen(request)

# 获取网站数据
content = response.read().decode("utf-8")

# 打印
print(content)



