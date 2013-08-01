# coding: utf-8
'''
Created on 2013-7-5
http://bt.ktxp.com/playbill.php
@author: xuechong
'''

import urllib2
from bs4 import BeautifulSoup
from utils import Commons
from google.appengine.api import memcache

#file_ = open("f:/contents.txt","r",-1)
#text = file_.read()
#file_.close()

url ="http://bt.ktxp.com/playbill.php"
def readContent():
    header ={'User-Agent':'mozilla/5.0 (windows; U; windows NT 5.1; zh-cn)'}
    req=urllib2.Request(url,None,header)
    response = urllib2.urlopen(req)
    page = response.read()
    return page

def decodeContent(content):
    soup = BeautifulSoup(content)
    _dtList = soup.find_all("dt")
    for dl in soup.find_all("dl"):
        print dl.find("dt").contents[0].encode("utf-8")
        for dd in dl.find_all("dd"):
            print dd.find("a").contents[0].encode("utf-8")
            
def todayContent():
    pass

def loadFromCache():
    
    pass

todayKey = lambda : "animeList" + str(Commons.todayStr())

if __name__ == '__main__':
    
    #decodeContent(readContent())
    print todayKey()
    pass
   