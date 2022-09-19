# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 10:26
# @Author : xwz

import urllib.request

# download 网页
url_page = 'http://www.baidu.com'
urllib.request.urlretrieve(url_page, 'baidu.html')

# download 图片
url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fhbimg.huabanimg.com%2F135f1c16978fa54d1950d15aabbfbd6173e5d9b5467a7-LaxwwR_fw658&refer=http%3A%2F%2Fhbimg.huabanimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665714788&t=12fe0350bff22dfb443c97088584dedf'
urllib.request.urlretrieve(url=url_img, filename='Victoria\'s Secret.jpg')

# download 视频
url_video = 'https://vd4.bdstatic.com/mda-ji0468kuf7uta8we/sc/mda-ji0468kuf7uta8we.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1663125140-0-0-defe72d09f70d67804e8aa51ad03f835&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=2540176649&vid=14783576046296535138&abtest=104378_1&klogid=2540176649'
urllib.request.urlretrieve(url_video, 'Peppa Pig.mp4')

