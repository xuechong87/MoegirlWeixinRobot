# coding: utf-8
'''
Created on 2013-7-5
http://bt.ktxp.com/playbill.php
@author: xuechong
'''

from bs4 import BeautifulSoup
from utils.Commons import fetchContentFromUrl 
from utils.Commons import todayStr
from google.appengine.api import memcache

#file_ = open("f:/contents.txt","r",-1)
#text = file_.read()
#file_.close()

url ="http://bt.ktxp.com/playbill.php"
getContent = lambda : fetchContentFromUrl(url)

def decodeContent(content):
    result= ""
    soup = BeautifulSoup(content)
    _dtList = soup.find_all("dt")
    for dl in soup.find_all("dl"):
        result = result + dl.find("dt").contents[0].encode("utf-8") + ":\r\n"
        for dd in dl.find_all("dd"):
            result = result +  dd.find("a").contents[0].encode("utf-8") + "\r\n"
    return result
            
def todayContent():
    pass

def loadFromCache():
    
    pass

todayKey = lambda : "animeList" + str(todayStr())

if __name__ == '__main__':
    
    #decodeContent(readContent())
    print todayKey()
    pass
   