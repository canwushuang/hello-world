#coding=utf8
import itchat, time, os, sched
from itchat.content import *
import urllib.request
import json
from urllib.parse import quote
import re


def getHtml(url):
        page = urllib.request.urlopen(url)
        html = page.read()
        return html
    
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):    
    #itchat.send('%s: %s' % ('我是鹦鹉', msg['Text']), msg['FromUserName'])
    #print('个人消息'+msg['FromUserName']+msg['Text'])
    
    if __name__ == '__main__':
 
        key = '8b56e859511033f22f307455f60b3964'
        api = 'http://www.tuling123.com/openapi/api?userid=853724&key=' + key + '&info='
        #while True:
        articles = []
        info = urllib.parse.quote(msg['Text'])
        request = api + info 
        response = getHtml(request)
        dic_json = json.loads(response)

        company_url_ = 'http://m.qixin.com/search/'
        if re.match('查询.*?[公司|事务所]' , msg['Text']):
                company_url_ = company_url_ +urllib.parse.quote(msg['Text'][2:])+'.html'
                itchat.send('%s: %s' % ('小AI\n', company_url_ ), msg['FromUserName'])
       # for alist in enumerate(dic_json['list']):
              #  articles.append(alist)
                #print ('机器人: ' + dic_json['text'] + info + str(type(info)) + str(type(api)))
        elif dic_json['code'] == 100000 :
                itchat.send('%s: %s' % ('小AI[愉快]', dic_json['text']), msg['FromUserName'])
                print(msg['Text'])
        elif dic_json['code'] == 200000 :
                itchat.send('%s: %s %s' % ('小AI[愉快]', dic_json['text'], dic_json['url']), msg['FromUserName'])
        else:
                content = dic_json['list']
                for i in range(10):  
                        articles.append(content[i]['article']+"\n")
                        articles.append(content[i]['detailurl']+"\n")
                itchat.send('%s: %s %s' % ('小AI[坏笑]', dic_json['text']+"\n", ''.join(articles[:]) ), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('hi~[愉快][愉快]我是微信机器人', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        if __name__ == '__main__':
 
                key = '8b56e859511033f22f307455f60b3964'
                api = 'http://www.tuling123.com/openapi/api?userid=853724&key=' + key + '&info='
                #while True:
                articles = []
                info = urllib.parse.quote(msg['Text'][5:])
                request = api + info 
                response = getHtml(request)
                dic_json = json.loads(response)
               # for alist in enumerate(dic_json['list']):
                      #  articles.append(alist)
                        #print ('机器人: ' + dic_json['text'] + info + str(type(info)) + str(type(api)))
                if dic_json['code'] == 100000 :
                        itchat.send('%s: %s' % ('小AI', dic_json['text']), msg['FromUserName'])
                elif dic_json['code'] == 200000 :
                        itchat.send('%s: %s %s' % ('小AI', dic_json['text'], dic_json['url']), msg['FromUserName'])
                else:
                        content = dic_json['list']
                        for i in range(10):  
                                articles.append(content[i]['article']+"\n")
                                articles.append(content[i]['detailurl']+"\n")
                        itchat.send('%s: %s %s' % ('小AI', dic_json['text']+"\n", ''.join(articles[:]) ), msg['FromUserName'])


itchat.auto_login(True)
itchat.run(debug=True)
