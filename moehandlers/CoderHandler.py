# coding: utf-8
'''
Created on 2013-7-7
the coder lao huang li!!! for moegirl wiki
@author: xuechong
'''
from google.appengine.api import memcache
from Weixin import textReply
import time
import logging
from utils.Commons import randomFromList

client = memcache.Client()
__coderCalenderKey__ = ""
__namespace__ = "coderCalender"

class CoderHandler():
    """
    the coder lao huang li!!! for moegirl wiki
    """
    @staticmethod
    def __helpkey__ ():
        return __coderCalenderKey__
    @staticmethod
    def __helpcontent__():
        return ""
    
    def handle(self,handlerChain):
        if handlerChain.getMsgContent() == __coderCalenderKey__:
            return textReply(handlerChain.userMsg,find())
        else:
            return handlerChain.invokeNext()
    
todayKey = lambda : "coderCalender" + time.strftime('%Y-%m-%d',time.localtime(time.time()))

def find():
    result =client.get(todayKey(), __namespace__)
    if result is None:
        result = addNew()
    return result

def addNew():
    logging.info("create new coder calender")
    content = newContent()
    client.set(key=todayKey(),\
               value = content,\
               time=24*60*60,\
               namespace=__namespace__)
    return content
_chong = ["Java","Python","C#","Javascript","Perl","C","C++",\
          "Delphi","Objective-c","Basic","PHP","Ruby","Pascal",\
          "Lisp","MATLAB","T-SQL","PL-SQL","GO","Lua","Erlang",\
          "Scala","Groovy","Smalltalk","F#","Fortran","ActionScript",\
          "Bash","Ada"]
_sha = ["Eclipse","Netbeans","Vim","Emacs","UltraEdit","Notepad++",\
        "EditPlus","SublimeText","VisualStudio","Delphi","Aptana",\
        "GCC","DreamWeaver","PowerDesigner","MySql","Oracle","DB2",\
        "MongoDB","SQLServer","Suse","Ubuntu","CentOS","WindowsServer",\
        "Excel","PhotoShop"]

_jy_style_ = ["面朝","躺在","跪在","坐在","站在","趴在","倒立在","背向"]
_jy_place_ = ["东南","西北","西南","东北","书桌","键盘","马扎","沙发","床","鼠标",\
              "显示器","平板电脑"]
_jy_ccontent_ = ["写设计文档","写单元测试","部署生产环境","重做系统","重构代码",""]
_j_detail_ = [""]
_y_detail_ = [""]

def newContent():
    return ""

if __name__ == "__main__":
    print todayKey()