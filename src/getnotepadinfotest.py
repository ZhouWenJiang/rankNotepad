#coding=utf-8
import urllib2;
from bs4 import BeautifulSoup;
import re
c=urllib2.urlopen('http://detail.zol.com.cn/381/380423/param.shtml');
content = c.read();
content = content.decode('gbk').encode('utf-8');
soup = BeautifulSoup(content, "html.parser");
print('_______________________________________________________________')
for element in soup.select(".param-name"):
    if cmp(element.string,u'CPU型号')==0:
        id=element.attrs['id'];
        num=id[id.find("_")+1]
        print id+"  "+num;
        print(soup.select("#newPmVal_"+num)[0].string)
        
list = soup.select('#page-title');
print list[0].string[:-2];