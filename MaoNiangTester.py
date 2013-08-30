'''
Created on 2013-8-21

@author: xuechong
'''
import webapp2
from Weixin import MsgContent
import logging
import Weixin
from google.appengine.api import xmpp
from httplib import responses

class MainProcessor(webapp2.RequestHandler):
    
    def get(self):
        param = self.request.get
        write = self.response.out.write
        self.response.headers['Content-Type'] = 'text/plain'
        if Weixin.validate(param):
            write(param("echostr"))
        else:
            write("what's up man -.-?")
        
    def post(self):
        #if Weixin.validate(self.request.get):
        logging.debug(self.request._body__get())
        write = self.response.out.write
        msg = MsgContent(self.request._body__get())
        chat_message_sent = False
        status_code = xmpp.send_message(from_jid=from_jid,jids=to_jid,body=msg.content,raw_xml=True)
        chat_message_sent = (status_code == xmpp.NO_ERROR)
        write(chat_message_sent)

app = webapp2.WSGIApplication([('/test', MainProcessor)])