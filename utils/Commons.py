# coding: utf-8
'''
Created on 2013-7-7

@author: xuechong
'''
import random
import datetime

randomFromList = lambda list_:list_[random.randint(0,len(list_)-1)]

todayStr = lambda :(datetime.datetime.utcnow() + datetime.timedelta(hours=+8)).strftime("%Y%m%d")
