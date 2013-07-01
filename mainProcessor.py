'''
Created on 2013-7-1

@author: xuechong
'''
import webapp2
import hashlib

weixin_token = "token"

class MainProcessor(webapp2.RequestHandler):
    
    def get(self):
        attr = self.request.__getattribute__()
        signature = attr("signature")
        timestamp = attr("timestamp")
        nonce = attr("nonce")
        echostr = attr("echostr")
        
        list_ = sorted([weixin_token, timestamp, nonce])
        sha1 = hashlib.sha1()
        sha1.update("".join(list_))
        
        self.response.headers['Content-Type'] = 'text/plain'
        write = self.response.out.write()
        if sha1.digest() == signature:
            write(echostr)
        else:
            write("error")
        
    def post(self):
        return

app = webapp2.WSGIApplication([('/', MainProcessor)])
