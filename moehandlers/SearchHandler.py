# coding: utf-8
'''
Created on 2013-8-7
search the moegirl wiki
@author: xuechong
'''
import MoeGirlWiki
import Weixin
import urllib 

__suf__="是什么"

class SearchHandler():
    @staticmethod
    def __helpkey__ ():
        return "搜索萌百"
    @staticmethod
    def __helpcontent__():
        return ""
    
    def handle(self,handlerChain):
        
        if (handlerChain.getMsgType()=="text"):
            content = handlerChain.getMsgContent()
            if hasKeyWord(content):
                searchKey = content[:content.rfind(__suf__)]
                resultList = MoeGirlWiki.searchTitle(searchKey)
                return Weixin.textReply(handlerChain.userMsg,buildReplyStr(resultList))
        return handlerChain.invokeNext()
    
def hasKeyWord(content):
    return (content !="" and content is not None) and content.endswith(__suf__)
    

def buildReplyStr(wikiList):
    if len(wikiList)>0:
        result = list()
        for subject in  wikiList:
            result.append(subject.title)
            result.append(u":\n")
            result.append(subject.snippet)
            result.append(u"\n")
            result.append(u"http://zh.moegirl.org/" + urllib.quote(subject.title))
            result.append(u"\n\n")
        if len(wikiList)>5:
            result.append(u"\n★更新姬提示★:\n搜索的结果有点多,可以尝试更多关键字搜索哦!")
        return (u"").join(result)
    else:
        return "人家不知道这种东西了啦"
        
    
    