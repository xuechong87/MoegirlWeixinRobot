'''
Created on 2013-7-1

@author: xuechong
'''
from google.appengine.api import xmpp

if __name__ == '__main__':
    user_address = 'moegirlwiki@nekonazo.com'
    chat_message_sent = False
    msg = "Someone has sent you a gift on Example.com. To view: http://example.com/gifts/"
    status_code = xmpp.send_message(user_address, msg)
    chat_message_sent = (status_code == xmpp.NO_ERROR)
    print chat_message_sent
