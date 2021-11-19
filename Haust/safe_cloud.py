# -*- coding: utf8 -*-
import requests
import time
import json


def safe():
    url = "https://yqfkfw.haust.edu.cn/smart-boot/api/healthReport/saveHealthReport"
    nowday = time.strftime("%Y-%m-%d %T", time.localtime())
    #now
    payload = json.dumps({
        "address": "河南省洛阳市涧西区联盟路",
        "age": "20",
        "bodyTemperature": 36,
        "createTime": "",
        "latitude": "34.65922",
        "longitude": "112.372713",
        "isStayLocal": 1,
        "phone": "填入手机号",
        "needUpdate": 1
    })
    header ={
        'Content-Type': 'application/json',
        'X-Id-Token': '填入token'
    }
    
    response = requests.request("POST", url, headers=header, data=payload)
    content=response.text[:-1]+',"time":'+nowday+"}"
    #开启推送请取消下面一行注释
    #push_wechat(content)


def push_wechat(content):
    #填入pushplus的token
    token = ''
    push_url = "http://www.pushplus.plus/send?token=" + token + "&title=报平安信息&content=" + content + "&template=json"
    requests.get(url=push_url)

#本程序放在腾讯云函数内执行
def main_handler(event, context):    
    safe()
