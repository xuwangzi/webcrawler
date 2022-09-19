# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 9:34
# @Author : xwz


# 使用urllib 获取Baidu首页源码
import urllib.request

# url
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发请求
# response请求
response = urllib.request.urlopen(url)

# 获取响应中的页面源码
# read 返回字节形式的二进制数据
# content内容
# 将二进制转换为字符串（解码 decode('编码格式')）
content = response.read().decode('utf-8')

# 打印数据
print(content)