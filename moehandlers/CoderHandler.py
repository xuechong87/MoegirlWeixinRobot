# coding: utf-8
'''
Created on 2013-7-7

@author: xuechong
'''
from google.appengine.api import memcache
import logging

client = memcache.Client()
__coderCalenderKey__ = ""

class CoderCal():
    @staticmethod
    def __helpkey__ ():
        return __coderCalenderKey__
    @staticmethod
    def __helpcontent__():
        return ""
    def handle(self,handlerChain):
        pass
    
def todayKey():
    return ""

def find():
    result =client.get(todayKey(), "coderCalender")
    if result is None:
        result = addNew()


def addNew():
    logging.info("create new coder calender")
    