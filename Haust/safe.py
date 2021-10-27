import requests
import json
import time


def safe():
    url = "https://yqfkfw.haust.edu.cn/smart-boot/api/healthReport/saveHealthReport"
    nowday = time.strftime("%Y-%m-%d %T", time.localtime())
    #填入对应信息
    payload = json.dumps({
        "address": "河南省洛阳市涧西区联盟路",
        "age": "20",
        "bodyTemperature": 36,
        "createTime": nowday,
        "latitude": "34.65922",
        "longitude": "112.372713",
        "isStayLocal": 1,
        #填入手机号
        "phone": "",
        "needUpdate": 1
    })
    headers = {
        'Content-Type': 'application/json',
        #将token放在这里
        'X-Id-Token': ''
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    #选择开启微信推送
    #push_wechat(response.text)
    return response.text


def push_wechat(content):
    #推送token
    token = ''

    push_url = "http://www.pushplus.plus/send?token=" + token + "&title=报平安信息&content=" + content + "&template=json"

    requests.get(url=push_url)


if __name__ == "__main__":
    safe()
