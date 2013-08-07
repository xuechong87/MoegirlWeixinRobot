# coding: utf-8
'''
Created on 2013-8-7
http://zh.moegirl.org/api.php?format=json&action=query&list=search&srwhat=title&srsearch=%E5%A4%8F%E5%A8%9C&srlimit=10
http://zh.moegirl.org/api.php?format=json&action=query&list=search&srwhat=text&srsearch=%E5%A8%9C
@author: xuechong
'''
from utils.Commons import fetchContentFromUrl
import json

_wikiurl = "http://zh.moegirl.org/api.php?format=json&action=query&list=search&srwhat=title&srsearch=$title&srlimit=$limit"

cleancontent = lambda x:str(x).replace("<span class='searchmatch'>", "").replace("</span>", "")


class WikiContent(object):
    title=""
    snippet=""
    size=""
    wordcount=""
    timestamp=""
    
if __name__ == '__main__':
    remoteResult = fetchContentFromUrl(_wikiurl.replace("$title", "夏娜").replace("$limit", "10"))
    print remoteResult + "\n"
    result = json.loads(remoteResult)
    allSubjects=result["query"]["search"]
    for subject in allSubjects:
        print "title=" + cleancontent(subject["title"]) + "\n"
        print "snippet=" + cleancontent(subject["snippet"]) + "\n"
        print "timestamp=" + str(subject["timestamp"]) + "\n"
    
    
    
    
    
    pass
    