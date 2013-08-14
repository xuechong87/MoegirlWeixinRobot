# coding: utf-8
'''
Created on 2013-8-14
search the newest page in moegirl wiki
@author: xuechong
'''

import Weixin
import logging

__event_key__ = "newest_pages"
class NewPageHandler(object):
   
    def handle(self,handlerChain):
        
        if (handlerChain.getMsgType()==Weixin.__MSGTYPE_EVENT__):
            if(handlerChain.getFromMsg("Event")==__event_key__):
                return Weixin.textReply(handlerChain.userMsg,"")
        
        return handlerChain.invokeNext()