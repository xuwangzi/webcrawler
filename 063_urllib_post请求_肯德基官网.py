# _*_ coding : utf-8 _*_
# @Time : 2022/9/15 9:12
# @Author : xwz


"""
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

post

'cname':'上海',
'pid':'',
'pageIndex':'1',
'pageSize':'10',
"""

import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname':'上海',
        'pid':'',
        'pageIndex':page,
        'pageSize':'10',
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    }

    request = urllib.request.Request(url=base_url, data=data, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def download_json(page, content):
    with open('kfc_第'+str(page)+'页.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('start page: '))
    end_page = int(input('end page: '))

    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        download_json(page, content)










