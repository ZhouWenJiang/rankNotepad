# coding=utf8
'''
Created on 2016年3月16日

@author: Zak
'''
import codecs

class rank:
    
    def __init__(self, file):
        self.rank = [];
        f =  codecs.open(file,'r','utf-8')
        for line in f:
            rankinfos = line.split("\t");
            self.rank.append(rankinfos[1].replace(" ","-"));
    
    def index(self, gpuname):
        for i in range(len(self.rank)):
            if cmp(self.rank[i],gpuname)==0:
                return i+1;
        return 10000;
    


gpurank = rank('gpurank.txt')


cpurank=rank('cpurank.txt')
