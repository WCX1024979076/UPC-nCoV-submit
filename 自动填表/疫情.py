import requests
import json,urllib,time,http
from bs4 import BeautifulSoup
try:
    filename = 'cookies.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)


    opener = urllib.request.build_opener(handler)
    with open("用户信息.txt",'r',encoding='utf8') as load_f:
        userinfo = json.load(load_f)
    params = urllib.parse.urlencode(userinfo)
    with opener.open('https://app.upc.edu.cn/uc/wap/login/check', data=bytes(params, 'utf-8')) as resp:
        print(resp.read().decode('utf-8'))
    cookie.save(ignore_discard=True, ignore_expires=True)


    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    with opener.open('https://app.upc.edu.cn/ncov/wap/default/index') as resp:
        soup = BeautifulSoup(resp.read().decode('utf-8'),features="html.parser")
        titles = soup.select("body  script") # CSS 选择器
        str1=titles[4].string
        result=json.loads(titles[4].string[str1.find("{"):str1.find("}",1600)+1])
        

    with open("result.json",'r',encoding='utf8') as load_f:
        load_dict = json.load(load_f)
    load_dict["created"]=result["created"]
    load_dict["date"]=result["date"]
    load_dict["id"]=result["id"]


    params = urllib.parse.urlencode(load_dict)
    with opener.open('https://app.upc.edu.cn/ncov/wap/default/save', data=bytes(params, 'utf-8')) as resp:
        print(resp.read().decode('utf-8'))
except :
    print("发生错误，请检查是否修改用户信息中的账号密码，如出现bug，请联系开发人员！！！")
finally :
    input("请输入回车继续")