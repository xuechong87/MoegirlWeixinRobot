# coding: utf-8
'''
Created on 2013-8-14

@author: xuechong
'''
import Weixin
import logging



class SubscribeHandler(object):
    
    __event_subscribe__ = "subscribe"#新的订阅
    __event_unsubscribe__ = "unsubscribe"
   
    def handle(self,handlerChain):
        
        if (handlerChain.getMsgType()==Weixin.__MSGTYPE_EVENT__):
            if(handlerChain.getFromMsg("Event")==SubscribeHandler.__event_subscribe__):
                logging.debug("new user!")
                return Weixin.textReply(handlerChain.userMsg,"从今天开始要好好相处哦!")
            
        return handlerChain.invokeNext()
    
pass

   
class NewPageHandler(object):
   
    __event_key__ = "newest_pages"
    def handle(self,handlerChain):
        
        if (handlerChain.getMsgType()==Weixin.__MSGTYPE_EVENT__):
            if(handlerChain.getFromMsg("Event")==NewPageHandler.__event_key__):
                return Weixin.textReply(handlerChain.userMsg,"")
        
        return handlerChain.invokeNext()    
    
    
pass    