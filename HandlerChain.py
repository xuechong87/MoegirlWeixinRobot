# coding: utf-8
'''
Created on 2013-7-3
handler chain
@author: xuechong
'''
from moehandlers.SellMoeHandler import SellMoeHandler
from Weixin import textReply
import logging

__default_chain__ = (SellMoeHandler,)

class HandlerChain(object):
    
    handlers = list()
    userMsg = None
    
    def __init__(self,userMsg):
        self.handlers=list(__default_chain__)
        logging.debug("new handlerChain" + str(self.handlers))
        self.userMsg = userMsg
        
    def doChain(self):
        result =  self.invokeNext()
        return result==None and textReply(self.userMsg) or result
    
    def invokeNext(self):
        result = None
        if len(self.handlers)>0:
            handler = self.handlers.pop()()
            result = handler.handle(self)
            if result==None and len(self.handlers)>0:
                result = self.invokeNext()
        return result
    
    