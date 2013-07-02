'''
Created on 2013-7-1

@author: xuechong
'''
import webapp2
import hashlib
from xmlread import MsgContent

weixin_token = "token"

class MainProcessor(webapp2.RequestHandler):
    
    def get(self):
        param = self.request.get
        write = self.response.out.write
        
        list_ = sorted([weixin_token, param("timestamp"), param("nonce")])
        sha1 = hashlib.sha1()
        sha1.update("".join(list_))
        
        self.response.headers['Content-Type'] = 'text/plain'
        
        if str(sha1.hexdigest()) == param("signature"):
            write(param("echostr"))
        else:
            write("what's up man -.-?")
        
    def post(self):
        write = self.response.out.write
        msg = MsgContent(self.request._body__get())
        result = "<xml>\
        <ToUserName><![CDATA[${toUser}]]></ToUserName>\
        <FromUserName><![CDATA[${fromUser}]]></FromUserName> \
        <CreateTime>${createTime}</CreateTime>\
        <MsgType><![CDATA[text]]></MsgType>\
        <Content><![CDATA[哈哈哈哈啊哈哈啊]]></Content>\
        <MsgId>${MsgId}</MsgId>\
        </xml>".replace("${toUser}", msg.get("ToUserName")).replace("${FromUserName}","")\
        .replace("${createTime}",msg.get("CreateTime")).replace("${MsgId}",msg.get("MsgId"))
        write(result)

app = webapp2.WSGIApplication([('/test', MainProcessor)])


