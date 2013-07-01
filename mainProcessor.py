'''
Created on 2013-7-1

@author: xuechong
'''
import webapp2
import hashlib

weixin_token = "token"

class MainProcessor(webapp2.RequestHandler):
    
    def get(self):
        param = self.request.get
        write = self.response.out.write
        
        list_ = sorted([weixin_token, param("timestamp"), param("nonce")])
        sha1 = hashlib.sha1()
        sha1.update("".join(list_))

        self.response.headers['Content-Type'] = 'text/plain'
        
        if sha1.digest() == param("signature"):
            write(param("echostr"))
        else:
            write("what's up man -.-?")
        
    def post(self):
        return self.get(self)

app = webapp2.WSGIApplication([('/weixin', MainProcessor)])
