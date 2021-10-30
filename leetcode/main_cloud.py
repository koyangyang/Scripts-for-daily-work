# -*- coding: utf8 -*-
import json
import requests

def getcontext():
    base_url = 'https://leetcode-cn.com'
    # 获取今日每日一题的题名(英文)
    response = requests.post(base_url + "/graphql", json={
        "operationName": "questionOfToday",
        "variables": {},
        "query": "query questionOfToday { todayRecord {   question {     questionFrontendId     questionTitleSlug     __typename   }   lastSubmission {     id     __typename   }   date   userStatus   __typename }}"
    })
    leetcodeTitle = json.loads(response.text).get('data').get('todayRecord')[0].get("question").get('questionTitleSlug')
    # 获取今日每日一题的所有信息
    url = base_url + "/problems/" + leetcodeTitle
    response = requests.post(base_url + "/graphql",
                             json={"operationName": "questionData", "variables": {"titleSlug": leetcodeTitle},
                                   "query": "query questionData($titleSlug: String!) {  question(titleSlug: $titleSlug) {    questionId    questionFrontendId    boundTopicId    title    titleSlug    content    translatedTitle    translatedContent    isPaidOnly    difficulty    likes    dislikes    isLiked    similarQuestions    contributors {      username      profileUrl      avatarUrl      __typename    }    langToValidPlayground    topicTags {      name      slug      translatedName      __typename    }    companyTagStats    codeSnippets {      lang      langSlug      code      __typename    }    stats    hints    solution {      id      canSeeDetail      __typename    }    status    sampleTestCase    metaData    judgerAvailable    judgeType    mysqlSchemas    enableRunCode    envInfo    book {      id      bookName      pressName      source      shortDescription      fullDescription      bookImgUrl      pressImgUrl      productUrl      __typename    }    isSubscribed    isDailyQuestion    dailyRecordStatus    editorType    ugcQuestionId    style    __typename  }}"})
    # 转化成json格式
    jsonText = json.loads(response.text).get('data').get("question")
    # 题目题号
    no = jsonText.get('questionFrontendId')
    # 题名（中文）
    leetcodeTitle = jsonText.get('translatedTitle')
    # 题目难度级别
    level = jsonText.get('difficulty')
    # 题目内容
    context = jsonText.get('translatedContent')
    # 数据全部HTML化
    htmlText = "<h3>" + no + "." + leetcodeTitle + "</h3>" + "<p><strong>" + level + "</strong></p>" + context

    return htmlText

def pushwechat(htmlText):
    #pushplus的token
    pushplus_token = ""
    a={"token":pushplus_token,"title":"LeetCode每日一题","content":htmlText,"template":"html"}
    urlp="http://www.pushplus.plus/send"
    requests.post(urlp,json=a)


def main_handler(event, context):
    htmlText = getcontext()
    pushwechat(htmlText)