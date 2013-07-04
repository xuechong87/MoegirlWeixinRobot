# coding: utf-8
'''
Created on 2013-7-4
@author: xuechong
'''
from __future__ import unicode_literals
import webapp2
from model.Flower import save
import logging

class FlowerProcessor(webapp2.RequestHandler):
    
    def post(self):
        self.get(self)
    def get(self):
        try:
            save("豆花","又叫豆腐脑")
            save("豆花(咸)","壮我大咸党!!!")
            save("豆花(甜)","甜党才是王道!!!")
            save("豆花(辣)","辣党万岁!!!")
        except Exception as e:
            logging.error(str(e))
            self.response.out.write(str(e))
        self.response.out.write("finish")

app = webapp2.WSGIApplication([('/flower', FlowerProcessor)])

