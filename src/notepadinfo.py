# coding=utf8
'''
Created on 2016年3月16日

@author: Zak
'''
import urllib2
from bs4 import BeautifulSoup;
from rank import cpurank, gpurank;

def has_class_but_no_id(tag):
    return tag.name == 'li' and tag.has_attr('data-follow-id')

def getnotepadlist(menuid, minprice=4000, maxprice=5000, pageno=1, cat=16):
    listurl = getlisturl(menuid, minprice, maxprice, pageno, cat);
    print listurl;
    soup = getsoup(listurl);
    product = [];
    for element in soup.find_all(has_class_but_no_id):
        price = element.select(".price-type")[0].string;
        product.append([element.attrs["data-follow-id"][1:], price])
        
    return product;

def getnotepadinfo(productid, params=[u'CPU型号', u'显卡芯片']):
    paramurl = getparamurl(productid);
    soup = getsoup(paramurl);
    
    notepadinfo = [ -1 for i in range(len(params) + 1)]
    
    list = soup.select('#page-title');
    # 名称
    notepadinfo[0] = list[0].string[:-2];
    # 其他参数
    
    for element in soup.select(".param-name"):
        for i in range(len(params)):
            if cmp(element.string, params[i]) == 0:
                id = element.attrs['id'];
                num = id[id.find("_") + 1:]
                notepadinfo[i + 1] = soup.select("#newPmVal_" + num)[0].string
        

    
    return notepadinfo;
    
    
def getsoup(url, charset='GBK'):
    c = urllib2.urlopen(url);
    content = c.read();
    content = content.decode(charset).encode('utf-8');
    soup = BeautifulSoup(content, "html.parser");
    return soup

def getlisturl(menuid, minprice=4000, maxprice=5000, pageno=1, cat=16):
    # http://detail.zol.com.cn/notebook_index/subcate16_160_list_1234-6700_5.html;
    return 'http://detail.zol.com.cn/notebook_index/subcate%d_%d_list_%d-%d_%d.html' % (cat, menuid, minprice, maxprice, pageno)
    #return 'http://detail.zol.com.cn/notebook_index/subcate%d_list_%d-%d_%d.html' % (cat, minprice, maxprice, pageno)

def getparamurl(productid):
    # http://detail.zol.com.cn/381/380423/param.shtml
    chnlid = int(productid) / 1000 + 1
    return 'http://detail.zol.com.cn/%d/%s/param.shtml' % (chnlid, productid)    


def preprocesscpu(name):
    # Intel 酷睿i5 5200U  
    if name.find("Intel") >= 0:
        name = name.replace(u'酷睿', 'Core ');
    name = name.replace(' ', "-");
    return name;

def preprocessgpu(name):
    # NVIDIA GeForce GT 740M＋Intel GMA HD 4400
    print name;
    index = name.find("+") 
    if index < 0:
        index = name.find(u'＋')
    if index >= 0:
        name = name[:index]
    name = name.replace(' ', "-");
    return name;


def my_cmp(data1, data2):
    
    gpucompare = cmp(data1[2], data2[2])
    if gpucompare != 0:
        return gpucompare;
    
    cpucompare = cmp(data1[1], data2[1])
    if cpucompare != 0:
        return cpucompare;
    
    return cmp(data1[3], data2[3]);
        
# list = [];   
# for i in range(15):
#     list.extend(getnotepadlist(160, minprice=3000, maxprice=4000, pageno=(i + 1)));
# 
# # 名称 CPU评测，GPU排行，价格
# data = [];
# for notepad in list:
#     try:
#         params = getnotepadinfo(notepad[0]);
#         print ",".join(params)+"    "+str(notepad[0]);
#         cpu = preprocesscpu(params[1]);
#         cpuscore = cpurank.index(cpu);
#         gpu = preprocessgpu(params[2]);
#         gpuscore = gpurank.index(gpu);
#         
#         print 'cpu:%s rank:%d gpu:%s,rank:%d' % (cpu, cpuscore, gpu, gpuscore);
#         data.append([params[0], cpuscore, gpuscore, notepad[1], cpu, gpu]);
#     except Exception, e:
#         print e;
# data.sort(cmp=my_cmp);
# print '______________________________________________________________________'
# for element in data:
#     print "%s\t%d\t%d\t%s\t%s\t%s" % tuple(element);


    
    
    
    
    
    
    
    
    
    
    
