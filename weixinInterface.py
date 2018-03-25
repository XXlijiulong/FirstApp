# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr = data.echostr
        #自己的token
        token="wudijingyingzhandui" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
        
	def POST(self):
        str_xml = web.data() 
        xml = etree.fromstring(str_xml)#进行XML解析
        mstype = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        
     
    	if msgType == 'text':
        	content=xml.find("Content").text
        	if(content == u"中秋"):
            	title1 = '知友们，中秋快乐！'
    			description1 = '给知友的祝福。'
    			xc = 'http://viewer.maka.im/k/J64391B8'
    			pic = 'http://pic33.nipic.com/20130923/11927319_180343313383_2.jpg'
    			return self.render.reply_pic(fromUser,toUser,title1,description1,pic,xc)
    	'''elif msgType == 'image':
        		pass'''

    		
        
        elif mstype == 'text':
            content = xml.find("Content").text#获得用户所输入的内容
            key = '7ed3193dea054afd892f3c9d3124c8ed'  ###图灵机器人的key' ###图灵机器人的key 
            api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='  
            info = content.encode('UTF-8') 
            url = api + info  
            page = urllib.urlopen(url)  
            html = page.read() 
            dic_json = json.loads(html)  
            reply_content = dic_json['text']
            return self.render.reply_text(fromUser,toUser,int(time.time()),reply_content)