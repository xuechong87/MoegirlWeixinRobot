# coding: utf-8
'''
Created on 2013-7-3

@author: xuechong
'''
import Weixin
import random

sellMoeList=["自动应答姬卖萌中~\(≧▽≦)/~啦啦啦","人家还只会卖萌了啦 (＞﹏＜)","自动应答姬努力卖萌中(oﾟωﾟo)","自动应答姬各种卖萌中(＞。☆)"]

class SellMoeHandler(object):
   
    def invoke(self,handlerChain):
        if(handlerChain.userMsg.get("MsgType")!="text"):
            return None
        
        answer = random.randint(0,len(sellMoeList)-1)
        return Weixin.textReply(handlerChain.userMsg,sellMoeList[answer])
    
    
    