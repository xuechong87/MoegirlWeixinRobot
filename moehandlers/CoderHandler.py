# coding: utf-8
'''
Created on 2013-7-7
the coder lao huang li!!! for moegirl wiki
@author: xuechong
'''
from google.appengine.api import memcache
from Weixin import textReply
import time
import logging
from utils.Commons import randomFromList

client = memcache.Client()
__coderCalenderKey__ = ""
__namespace__ = "coderCalender"

class CoderCalender():
    """
    the coder lao huang li!!! for moegirl wiki
    """
    @staticmethod
    def __helpkey__ ():
        return __coderCalenderKey__
    @staticmethod
    def __helpcontent__():
        return ""
    
    def handle(self,handlerChain):
        if handlerChain.getMsgContent() == __coderCalenderKey__:
            return textReply(handlerChain.userMsg,find())
        else:
            return handlerChain.invokeNext()
    
todayKey = lambda : "coderCalender" + time.strftime('%Y-%m-%d',time.localtime(time.time()))

def find():
    result =client.get(todayKey(), __namespace__)
    if result is None:
        result = addNew()
    return result

def addNew():
    logging.info("create new coder calender")
    content = newContent()
    client.set(key=todayKey(),\
               value = content,\
               time=24*60*60,\
               namespace=__namespace__)
    return content

def newContent():
    return ""

if __name__ == "__main__":
    print todayKey()