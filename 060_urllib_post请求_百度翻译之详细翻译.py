# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 16:19
# @Author : xwz

import urllib.request
import urllib.parse

# 找到对应的接口
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Host':'fanyi.baidu.com',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    # 'Accept':'*/*',
    # 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Acs-Token':'1663138990327_1663154433986_MxjBoE0r+NAA3MJVqA0jS7ES9lwiKxG4c7OQPGIkrd4WOHNuEaLiBHjWM+nFPDQ/UrDXkJoDqDIY4K8ukdBbInnUFVVboc9aZVSoejbrSaGZ0BUDtB4N/PumWd/uoP2f1BkOP5Q0nv+FCRrT/sbzDjYbhvqtON2OJAK2Wxz+/F4gkN2msJwgHKned2JA5eSqaRV23/5SntgOFOE5dHSAf8isITUh/CnEkEFT9ooekllBS6q8p0xyA/7NJvKV16ORd5eWKIPB6tG5qLHbtx6uLs5BCYE6eHizo8CCaxNx87Q=',
    # 'X-Requested-With':'XMLHttpRequest',
    # 'Content-Length':'135',
    # 'Origin':'https://fanyi.baidu.com',
    # 'Connection':'keep-alive',
    # 'Referer':'https://fanyi.baidu.com/?aldtype=16047',
    'Cookie':'BAIDUID=9C45DE2B60B14D69FDCE278F9B6E1D2D:FG=1; BIDUPSID=9C45DE2B60B14D692D4C2E32F369B993; PSTM=1647220824; BDUSS=FHZ1JZcmFKZ2lSaXpYOXlpZEhGR2FTTzVuZzEzTHlZTWRRb2dlaFNBSjJZM3hpSVFBQUFBJCQAAAAAAAAAAAEAAADfwGFFNTQxNjEyNzY3YQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHbWVGJ21lRiLX; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1663154422; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=37146_36545_36459_37117_36885_34812_37260_26350_37285_37364; ab_sr=1.0.1_OGNiMWFmZmIyMzkyYjRkZDUzZmMwNDg5MGQwMjlmOGVmMzhjOWNlNDIxODM2ZjIyMWI3NDdhNDliNjZkYzIyMzliY2QxZGM2NTQyMDM1ZjVlNzAyMTE5OWE1ZjM2MWRlMzFkMzc4MDU0NGQwNDlhMjJmYzU2Y2Q4MThhZTc3MjdiNGJmZGQ2MjI5MzRiOTNiYzlhMmQ5N2Q4ODVjMTE0NWUyYjY4ZjQ0ZTQxNmVhMmI5NjRkYzRjZWZiYjExMTlm; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; delPer=0; PSINO=5; BA_HECTOR=802084842k01ak20ah043f911hi3caq19; ZFY=lA5MeRxbTiWOuD:AP4uX1tHLphg9vwNb0SIgxXlWZJuU:C; ZD_ENTRY=baidu; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1663154422; APPGUIDE_10_0_2=1',
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-origin',
}

data = {
    'from':'en',
    'to':'zh',
    'query':'love',
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'198772.518981',
    'token':'df5b27624c59cbeda75d174d4d3dffa0',
    'domain':'common',
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

# str字符串 => json对象
import json

obj = json.loads(content)
print(type(obj))
print(obj)










