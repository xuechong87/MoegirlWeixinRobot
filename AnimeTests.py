'''
Created on 2013-7-5
http://bt.ktxp.com/playbill.php
@author: Administrator
'''
import urllib2

url ="http://bt.ktxp.com/playbill.php"
def readContent():
    header ={'User-Agent':'mozilla/5.0 (windows; U; windows NT 5.1; zh-cn)'}
    req=urllib2.Request(url,None,header)
    response = urllib2.urlopen(req)
    page = response.read()
    return page
    
if __name__ == '__main__':
    print (readContent())