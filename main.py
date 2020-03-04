#!/usr/bin/python
# -*- coding:UTF-8 -*-
# DB Forum - a buggy web forum server backed by a good database
from __future__ import unicode_literals
import chardet

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# The forumdb module is where the database interface code goes.
import forumdb

# Other modules used to run a web server.
import random 
import difflib
import argparse
from bs4 import BeautifulSoup
from beaker.middleware import SessionMiddleware
from bottle import *
from bottle import run,route,template,request,response,default_app,get,redirect
from bcrypt import hashpw
import bcrypt
import requests
import chardet
 

# 检查序号是否<0，以及是否大于句子最大数值
def checkNum(num):
    if num<0:
        return True
    if num>40:
        return True

#@hook('before_request')
#def setup_request():
#    request.session = request.environ['beaker.session']

@route('/registered')
def register():
    return template('register')

@route('/registered', method='get')
def register():
    addUser=forumdb.AddUser(username = request.query.username, password = password_crypt(request.query.password))
    username = request.query.username
    password = request.query.password
    password = password_crypt(password)
    response.set_cookie("username", username, secret='ukey')
    
    time = str(0)
    GetQuestions = forumdb.GetQuestions()
    GetAnswers = forumdb.GetAnswers()
    number=0
    return template(
                    'view',number = number, time=time,
                    question = GetQuestions[number]['ChineseSentences'], 
                    answer = GetAnswers[number]['EnglishSentences']
                   )

@route('/login')
def index():
    return template('login')

@route('/login', method = 'get')
def index():
    
    username = request.query.username
    password = request.query.password
    password = password_crypt(password)
    userInfo = forumdb.login(username,password)
    if userInfo!=[]:
        time = int(userInfo[0])
        sentenceNum = int(userInfo[1])
        response.set_cookie("username", username, secret='ukey')
        response.set_cookie("sentenceNum", str(sentenceNum))
        response.set_cookie("time", str(time))
        
        GetQuestions = forumdb.GetQuestions()
        GetAnswers = forumdb.GetAnswers()
        number = sentenceNum
        return template(
                    'view',number = number, time=time,
                    question = GetQuestions[number]['ChineseSentences'], 
                    answer = GetAnswers[number]['EnglishSentences']
                   )
    else:
        return redirect('/login')  
        

# page for now    
@route('/view', method = 'get')
def view():
    username = request.get_cookie("username", secret='ukey')
    time = forumdb.getTime(username)[0]['time']
    GetQuestions = forumdb.GetQuestions()
    GetAnswers = forumdb.GetAnswers()
    number = 0
    return template(
                    'view',number = number, time=time,
                    question = GetQuestions[number]['ChineseSentences'], 
                    answer = GetAnswers[number]['EnglishSentences']
                   )

# page for next sentence
@route('/goto/<sentNumber>')
def viewgoto(sentNumber):
    username = request.get_cookie("username", secret='ukey')
    time = forumdb.getTime(username)[0]['time']
    
    number = int(sentNumber) +1
    if checkNum(number):
        return "没有下一句了，<a href='/goto/39'>点此回到最后一句<//a>"
    GetQuestions = forumdb.GetQuestions()
    GetAnswers = forumdb.GetAnswers()
    return template('view',number = number, time=time,
                    question = GetQuestions[number]['ChineseSentences'], 
                    answer = GetAnswers[number]['EnglishSentences'])

# page for last sentence
@route('/returnto/<sentNumber>')
def viewReturnTo(sentNumber):
    username = request.get_cookie("username", secret='ukey')
    time = forumdb.getTime(username)[0]['time']
    #if request.get_cookie('timer'):
    #    time = request.get_cookie("timer")
    number = int(sentNumber) - 1
    if checkNum(number):
        return "没有上一页了，<a href='/view'>点此回到首页<//a>"
    GetQuestions = forumdb.GetQuestions()
    GetAnswers = forumdb.GetAnswers()
    return template('view',number = number, time=time,
                    question = GetQuestions[number]['ChineseSentences'], 
                    answer = GetAnswers[number]['EnglishSentences'])

# page for certain type of questions 
@route('/sentence/<senType>')
def viewGoTo(senType):
    username = request.get_cookie("username", secret='ukey')
    time = forumdb.getTime(username)[0]['time']
    
    number = int(senType) 
    GetQuestions = forumdb.GetQuestions()
    GetAnswers = forumdb.GetAnswers()
    return template('view', time=time,
                    question = GetQuestions[number]['ChineseSentences'], 
                    answer = GetAnswers[number]['EnglishSentences'], number = number)

# page for results
@route('/viewresult/<senNumber>', method='get')
def ViewResult(senNumber):
    username = request.get_cookie("username", secret='ukey')
    #timeOld = int(request.get_cookie("time"))
    #time = int(request.get_cookie("timer",str(timeOld)))
    #time = int(request.get_cookie("time", '0'))
    #response.set_cookie("timer", str(time))
    time = forumdb.getTime(username)[0]['time']
     
    number = int(senNumber)
    posts = request.query.content
    print(posts)
    length = len(posts)
    # If length is zero, post is empty - don't save it.
    if length > 0:
        forumdb.AddPost(posts)
        time = int(time) + 1
        #update time
        forumdb.updateTime(username,time)
    GetAnswers = forumdb.GetAnswers()
    posts = forumdb.GetAllPosts()[0]
    result = compare_file(GetAnswers[number]['EnglishSentences'],str(posts['content']))
    changed = extractSentences(result)[0]
    Answer  = extractSentences(result)[1]
    return template('viewresult', changed = changed, answer = GetAnswers[number]['EnglishSentences'],number=number)
'''
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
'''
# read two sentences to compare two sentences
def read_file(file_name):
    try:
        # 读取后按行分割
        text = file_name.splitlines()
        return text
    except IOError as error:
        print('Read input file Error: {0}'.format(error))
        sys.exit()

# 比较两个文件并把结果生成一份html文本
def compare_file(file1, file2):
    if file1 == "" or file2 == "":
        print('文件路径不能为空：第一个文件的路径：{0}, 第二个文件的路径：{1} .'.format(file1, file2))
        sys.exit()
    else:
        print("正在比较文件{0} 和 {1}".format(file1, file2))
    text1_lines = read_file(file2)
    text2_lines = read_file(file1)
    
    diff = difflib.HtmlDiff()    # 创建HtmlDiff 对象
    result = diff.make_table(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果
    return result

# 解析所需的内容
def extractSentences(html):
    import re
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    sentence1 = soup.find_all("#difflib_chg_to0__top")
    sentence2 = soup.td.parent.contents
    content = []
    for i, child in enumerate(sentence2):
        content.append(child)
        
    return content[-4],content[-1]

def password_crypt(password):
    SALT = b'$2b$10$8g62hrrYx4W11cQTuvi5ye'
    password = password.encode()
    cry_pwd = hashpw(password, SALT)
    return cry_pwd.decode()
        
if __name__ == '__main__':
    session_opts = {
   'session.type':'file',              #以文件的方式保存session
   'session.data_dir':'sessions',         #session保存目录
   'session.auto':True,               #自动保存session
   'session.domain':'0.0.0.0:8088'
    }
    app_argv = SessionMiddleware(default_app(),session_opts)
    run(app=app_argv, host='0.0.0.0', port=8088, debug=True, reloader=True)
    print('I am listening')
else:
    application = SessionMiddleware(default_app())
    
