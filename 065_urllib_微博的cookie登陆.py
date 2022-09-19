# _*_ coding : utf-8 _*_
# @Time : 2022/9/15 9:50
# @Author : xwz


# 个人信息页面是utf-8  但跳转到了登录页面（不是utf-8）
# 因为headers不完整，所以登陆不成功

import urllib.request

url = 'https://weibo.com/7517602527/profile'

headers = {
    'Host': 'weibo.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # cookie中携带登录信息，有登陆后的cookie就可以进入任何页面
    'Cookie': 'UOR=www.bilibili.com,service.weibo.com,www.bilibili.com; SINAGLOBAL=9482205803322.367.1660222649014; ULV=1663225418087:2:1:1:9371196324278.09.1663225418086:1660222649065; PC_TOKEN=f8b159bb72; SUB=_2A25OJqDWDeRhGeFL6lUX8CzJyTuIHXVtVZUerDV8PUNbmtAKLUbtkW9NQnHYyiag6817o7MftEbXgGmTo6sQcTvJ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhxcA1O.PqsBPQuRjYmZjUy5JpX5KzhUgL.FoMfeKMcehzfeoM2dJLoIp-LxK-LB.-L1K5LxKML12-L12iKxHzt; XSRF-TOKEN=n4C5HLv75afdgDKK3h2csjqm; WBPSESS=eyDLPcU90tHVPRrsWrtAPlpBDoaZdXtdan4Gf0BoMOtTT9B5HU6ZJWV6vJdWo28hEI4GndB30vmgmKQHRTQsfmDuR5y4UaiFpcWxhWLBEYoieMZE7PAzqdNjEXgnviVsiKukV3XH4kCfgDH_aSUTKM4tIY9KB7Gh0oyMZ6fDve0=; login_sid_t=01cec7ec44636d3acf33492709d8075a; cross_origin_proto=SSL; _s_tentry=weibo.com; wb_view_log=1408*7921.3636363636363635; Apache=9371196324278.09.1663225418086; ALF=1694761990; SSOLoginState=1663225991; wvr=6; wb_view_log_7517602527=1408*7921.3636363636363635; webim_unReadCount=%7B%22time%22%3A1663226617302%2C%22dm_pub_total%22%3A3%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A36%2C%22msgbox%22%3A0%7D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

with open('微博个人页面.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
