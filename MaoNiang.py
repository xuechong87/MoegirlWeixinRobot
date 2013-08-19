'''
Created on 2013-8-19
the maoniang apis
@author: xuechong
'''

from google.appengine.ext import db

class MaoNianMsg(db.Model):
    
    userId=db.StringProperty()
    msgId=db.StringProperty()
    msgContent=db.StringProperty()
    
    def __init__(self,userId,msgId,msgContent):
        self.userId = userId
        self.msgId = msgId
        self.msgContent = msgContent
        
    