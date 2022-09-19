# _*_ coding : utf-8 _*_
# @Time : 2022/9/15 17:01
# @Author : xwz

from lxml import etree

# xpath解析
# （1）本地文件                                               etree.parse
# （2）服务器响应的数据   response.read().decode('utf-8')      etree.HTML()

# （1）xpath解析：本地文件
tree = etree.parse('xpath解析案例.html')
print('tree: ')
print(tree)

print('---------------------------')

# 查找ul下的li
li_list = tree.xpath('//body/ul/li')
print('li_list: ')
print(li_list)
print('len(li_list): ')
print(len(li_list))

print('---------------------------')

# 查找所有有id的属性的li标签
li_list = tree.xpath('//li[@id]/text()')
print('li_list: ')
print(li_list)
print('len(li_list): ')
print(len(li_list))

print('---------------------------')

# 找到id=111的标签
li_list = tree.xpath('//li[@id="111"]/text()')  # 单引号里用双引号
print('li_list: ')
print(li_list)
print('len(li_list): ')
print(len(li_list))

print('---------------------------')

# 找到id=111的标签的属性值
li_list = tree.xpath('//li[@id="111"]/@class')
print('li_list: ')
print(li_list)
print('len(li_list): ')
print(len(li_list))

print('---------------------------')

# 找到id中包含1的标签
li_list = tree.xpath('//li[contains(@id,"1")]/text()')
print('li_list: ')
print(li_list)
print('len(li_list): ')
print(len(li_list))

print('---------------------------')

# 找到id中以2开头的标签
li_list = tree.xpath('//li[starts-with(@id,"2")]/text()')
print('li_list: ')
print(li_list)
print('len(li_list): ')
print(len(li_list))

print('---------------------------')

# 找到id中包含1 "且" id中以2开头的标签
li_list = tree.xpath('//li[contains(@id,"1") and starts-with(@id,"2")]/text()')
print('li_list: ')
print(li_list)
print('len(li_list): ')
print(len(li_list))

print('---------------------------')





