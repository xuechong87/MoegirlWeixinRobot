# coding: utf-8
'''
Created on 2013-8-7
search the moegirl wiki
@author: xuechong
'''
import MoeGirlWiki
import Weixin

__suf__="是什么"

class SearchHandler():
    @staticmethod
    def __helpkey__ ():
        return ""
    @staticmethod
    def __helpcontent__():
        return ""
    
    def handle(self,handlerChain):
        
        if (handlerChain.getMsgType()=="text"):
            content = handlerChain.getMsgContent()
            if hasKeyWord(content):
                searchKey = content[:-3]
                resultList = MoeGirlWiki.searchTitle(searchKey)
                return Weixin.textReply(handlerChain.userMsg,buildReplyStr(resultList))
        return handlerChain.invokeNext()
    
def hasKeyWord(content):
    return (content !="" and content is not None) and content.endswith(__suf__)
    

def buildReplyStr(wikiList):
    for subject in  wikiList:
        pass
        
    
    