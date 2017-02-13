#coding=utf-8
import urllib2
import html5lib
from html5lib import sanitizer
from html5lib import treebuilders
from bs4 import BeautifulSoup;
import re
c=urllib2.urlopen('http://detail.zol.com.cn/notebook_index/subcate16_160_list_1234-6700_5.html');
content = c.read();
content = content.decode("GBK").encode('utf-8');
#print content;
soup = BeautifulSoup(content, "html.parser");
def has_class_but_no_id(tag):
    return tag.name=='li' and tag.has_attr('data-follow-id')

print('_______________________________________________________________')
for element in soup.find_all(has_class_but_no_id):
    print(element.attrs["data-follow-id"])
    price = element.select(".price-type");
    print price[0].string
