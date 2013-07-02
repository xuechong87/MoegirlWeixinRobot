'''
Created on 2013-6-9
read xml
@author: Administrator
'''
from xml.etree import ElementTree

class MsgContent:
    
    content = {}
    
    def __init__(self,xmlContent):
        '''
        xmlContent the str content of the xml
        '''
        root = ElementTree.fromstring(xmlContent)
        _nodes = root.getiterator("xml")
        for node in _nodes.pop().getchildren():
            self.content[node.tag]=node.text
    
    def get(self,key):
        return self.content.get(key)
    
xmlPath = "F:\\weixin.xml";

def getXml(path):
    xmlContent = open(path).read()
    return MsgContent(xmlContent)

if __name__ == "__main__":
    print getXml(xmlPath).get("MsgType")
    