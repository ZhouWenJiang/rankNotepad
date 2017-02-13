# coding=utf8
'''
Created on 2016年3月16日

@author: Zak
'''
from notepadinfo import *;
# Start 参数设置
pageSize = 15;#获取的总页数
_menuId = 223;#品牌Id，联想：160，惠普：223，苹果：544，
_minprice = 3000;#最低价格
_maxprice = 4000;#最高价格
# end参数设置
list = [];   
for i in range(pageSize):
    list.extend(getnotepadlist(menuid=_menuId, minprice=_minprice, maxprice=_maxprice, pageno=(i + 1)));

# 名称 CPU排行，GPU排行，价格
data = [];
for notepad in list:
    try:
        params = getnotepadinfo(notepad[0]);
        print ",".join(params)+"    "+str(notepad[0]);
        cpu = preprocesscpu(params[1]);
        cpuscore = cpurank.index(cpu);
        gpu = preprocessgpu(params[2]);
        gpuscore = gpurank.index(gpu);
        
        print 'cpu:%s rank:%d gpu:%s,rank:%d' % (cpu, cpuscore, gpu, gpuscore);
        data.append([params[0], cpuscore, gpuscore, notepad[1], cpu, gpu]);
    except Exception, e:
        print e;
data.sort(cmp=my_cmp);
print '______________________________________________________________________'
for element in data:
    print "%s\t%d\t%d\t%s\t%s\t%s" % tuple(element);