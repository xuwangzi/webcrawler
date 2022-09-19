# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 20:18
# @Author : xwz


# 难点在于找接口
# https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=40&limit=20
# https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=60&limit=20

import urllib.parse
import urllib.request


def create_request(page):
    # url
    url_base = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&'

    data = {
        'start': (page-1)*20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)

    url = url_base + data

    # headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    }

    # 请求对象定制
    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    # 模拟浏览器向服务器发起请求
    response = urllib.request.urlopen(request)
    # 获取网站数据
    content = response.read().decode("utf-8")

    return content


def download_json(page, content):
    with open('豆瓣情色评分_第' + str(page) + '页.json', 'w', encoding='utf8') as fp:
        fp.write(content)



# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码'))

    # 每一页都有自己的请求对象定制
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        download_json(page, content)








