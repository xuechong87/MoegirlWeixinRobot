# coding: utf-8
'''
Created on 2013-7-1

@author: xuechong
'''
import webapp2
from Weixin import MsgContent
import logging
import Weixin
from HandlerChain import HandlerChain
from moehandlers import __test_chain__

class TestProcessor(webapp2.RequestHandler):
    
    
    def get(self):
        logging.info("get")
        param = self.request.get
        write = self.response.out.write
        logP = lambda x: logging.info(x + "|" + param(x))
        
        logP('token')
        logP('timestamp')
        logP('nonce')
        logP('signature')
        logP('echostr')
        
        self.response.headers['Content-Type'] = 'text/plain'
        if Weixin.validate(param):
            write(param("echostr"))
        else:
            write("what's up man -.-?")
        
    def post(self):
        logging.info("post")
        #if Weixin.validate(self.request.get):
        logging.debug(self.request._body__get())
        write = self.response.out.write
        msg = MsgContent(self.request._body__get())
        chain = list(__test_chain__)
        handlerChain= HandlerChain(userMsg=msg,handlerList=chain)
        write(handlerChain.doChain())

app = webapp2.WSGIApplication([('/test', TestProcessor)])


