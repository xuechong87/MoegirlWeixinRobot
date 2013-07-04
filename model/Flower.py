# coding: utf-8
'''
Created on 2013-7-4

@author: xuechong
'''
from google.appengine.ext import db
from google.appengine.ext import search

class Flower(search.SearchableModel):
    
    name = db.StringProperty()
    content = db.StringProperty()
    
    def description(self):
        result = str(self.name) + ":\n" + str(self.content) + "\n"
        return result.encode("utf-8")
    @classmethod
    def SearchableProperties(cls):
        return [['name'],search.ALL_PROPERTIES]
    
    
def save(name,content):
    flower = Flower()
    flower._key_name = name
    flower.content = content
    flower.name = name
    flower.put()

    
def findByName(searchStr):
    query = Flower.all()
    query.search(searchStr, properties=['name'])
    return query.fetch(20)

