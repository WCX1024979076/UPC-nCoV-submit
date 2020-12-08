try :
    import requests
    import json,urllib,time,http

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

    headers1 = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',)
    headers2=('X-Requested-With', 'XMLHttpRequest')
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    opener.addheaders = [headers1,headers2]

    with opener.open('https://app.upc.edu.cn/ncov/wap/default/index') as resp:
        result=json.loads(resp.read().decode("utf8"))['d']['info']
        
    with open("result.json",'r',encoding='utf8') as load_f:
        load_dict = json.load(load_f)
    load_dict["created"]=result["created"]
    load_dict["date"]=time.strftime("%Y%m%d", time.localtime())
    load_dict["id"]=result["id"]


    params = urllib.parse.urlencode(load_dict)
    with opener.open('https://app.upc.edu.cn/ncov/wap/default/save', data=bytes(params, 'utf-8')) as resp:
        print(resp.read().decode('utf-8'))
except :
    print("发生错误，请修改用户信息.txt")
input("请按任意键继续")
