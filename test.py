# coding=utf-8
import requests
import urllib
import json
import math
from selenium import webdriver
import mariadb
import sys
import time
from pytz import timezone
from datetime import datetime
import smtplib, ssl

# driver= webdriver.Chrome()


headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
           'cache-control': 'no-cache',
           'Connection': 'keep-alive',
           'Cookie': 'device_id=8233e6094954d1a2168054b4726bf1d2; s=de12605q09; __utmz=1.1594306298.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); xq_a_token=69a6c81b73f854a856169c9aab6cd45348ae1299; xqat=69a6c81b73f854a856169c9aab6cd45348ae1299; xq_r_token=08a169936f6c0c1b6ee5078ea407bb28f28efecf; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU5ODMyMzAwNCwiY3RtIjoxNTk2MDM1NDg1ODE4LCJjaWQiOiJkOWQwbjRBWnVwIn0.QmvumiJUTUHuffLabLv0ZXkWpCulcWn-HZHcyD9yVGV1oYae3VFfLJA0gpGxU6JLTs7zI_MO_UTK8i__1Cb-DsPpJK8inN_quDyUlgI2678o-UvuBpoZScC11ZVwwfZNA07dKjHeZQ1F0v9eD9LMztemuE8VDjv9biQoRunTFJtX7X88YIMDAeBZj-5k3buNPCwa7qu2nhkzy3MbrV67Y_Ig8inTmTUaZ8e2Bs2sNoV8aOqQL-ADvTtpB0d4Jd3kHWGbfa0hIYnvnW8Ftn9AbVZLp5zlMfgUMvfzeseviju_A6NlZGZmiDXtfPn6xzZQuXhgGDttgtBO-n84wFvv1Q; u=411596035500776; Hm_lvt_1db88642e346389874251b5a1eded6e3=1594391551,1594431706,1594647250,1596035502; __utmc=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1596058025; __utma=1.1930711503.1594306298.1596056716.1596069689.4; __utmt=1; __utmb=1.1.10.1596069689',
           'Host': 'xueqiu.com',
           'Referer': 'https://xueqiu.com/hq',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}

chinese_param = {'page': '1',
         'size': '30',
         'order': 'desc',
         'orderby': 'percent',
         'order_by': 'percent',
         'market': 'CN',
         'type': 'sh_sz',
         '_': '1596082598401'
         }

two = {'page': '1',
       'size': '30',
       'order': 'desc',
       'orderby': 'percent',
       'order_by': 'percent',
       'market': 'CN',
       'type': 'sh_sz',
       '_': '1596082598401',
       'Accept': '*/*',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
       'cache-control': 'no-cache',
       'Connection': 'keep-alive',
       'Cookie': 'device_id=8233e6094954d1a2168054b4726bf1d2; s=de12605q09; __utmz=1.1594306298.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); xq_a_token=69a6c81b73f854a856169c9aab6cd45348ae1299; xqat=69a6c81b73f854a856169c9aab6cd45348ae1299; xq_r_token=08a169936f6c0c1b6ee5078ea407bb28f28efecf; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU5ODMyMzAwNCwiY3RtIjoxNTk2MDM1NDg1ODE4LCJjaWQiOiJkOWQwbjRBWnVwIn0.QmvumiJUTUHuffLabLv0ZXkWpCulcWn-HZHcyD9yVGV1oYae3VFfLJA0gpGxU6JLTs7zI_MO_UTK8i__1Cb-DsPpJK8inN_quDyUlgI2678o-UvuBpoZScC11ZVwwfZNA07dKjHeZQ1F0v9eD9LMztemuE8VDjv9biQoRunTFJtX7X88YIMDAeBZj-5k3buNPCwa7qu2nhkzy3MbrV67Y_Ig8inTmTUaZ8e2Bs2sNoV8aOqQL-ADvTtpB0d4Jd3kHWGbfa0hIYnvnW8Ftn9AbVZLp5zlMfgUMvfzeseviju_A6NlZGZmiDXtfPn6xzZQuXhgGDttgtBO-n84wFvv1Q; u=411596035500776; Hm_lvt_1db88642e346389874251b5a1eded6e3=1594391551,1594431706,1594647250,1596035502; __utmc=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1596058025; __utma=1.1930711503.1594306298.1596056716.1596069689.4; __utmt=1; __utmb=1.1.10.1596069689',
       'Host': 'xueqiu.com',
       'Referer': 'https://xueqiu.com/hq',
       'Sec-Fetch-Dest': 'empty',
       'Sec-Fetch-Mode': 'cors',
       'Sec-Fetch-Site': 'same-origin',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
       'X-Requested-With': 'XMLHttpRequest'

       }

morning_market_start = '09:30'
morning_market_end = '11:30'
afternoon_market_start = '13:00'
afternoon_market_end = '15:00'


def main():
    url = "https://xueqiu.com/hq#exchange=CN&firstName=1&secondName=1_0"
    url2 = "https://xueqiu.com/service/v5/stock/screener/quote/list"
    url3 = "https://xueqiu.com/service/v5/stock/screener/quote/list?page=2&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1596069689183"
    connetMariaDB()
    warning=retrievingData()
    email(warning)

    #print(getAllStocks(url2))
    #while True:
        #programSleep()
        #crawlerDriver(url2)

    #insertDictData(getAllStocks(url2))
    print("done")


def email(newMessage):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "frontierstudio99@gmail.com"
    receiver_email="sunmingzhe99@gmail.com"
    password = "TESTtest1234!@#$"
    message = """\
    Subject: Hi there

    This message is sent from Python."""
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        #server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        #server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, newMessage)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()



def connetMariaDB():
    try:
        conn = mariadb.connect(
            user="itx",
            password="SMZsunmingzhe19@$",
            host="192.168.2.111",
            port=3307,
            database="test_database"

        )
        print("Successfully Connect to MariaDB")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    global cur
    cur = conn.cursor()

def insertDictData(stock):
        for mydict in stock:
            placeholders = ', '.join(['%s'] * len(mydict))
            columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
            values = ', '.join("'" + str(x).replace('None','0') + "'" for x in mydict.values())
            try:
                cur.execute("INSERT INTO %s ( %s ) VALUES ( %s );" % ('test_stock_data', columns, values)) #select table name here
            except mariadb.Error as e:
               print(f"Error: {e}")

def retrievingData():
    cur.execute(
        "SELECT time,symbol,amplitude,current FROM test_stock_data WHERE time LIKE ? AND amplitude>=?",
        ("2020-08-21%",10))

    message = "Current Stock Warning List\n\n\n"
    for (time,symbol,amplitude,current) in cur:
        newMess = f"Time: {time}, Symbol: {symbol},Amplitude: {amplitude}, Current: {current} \n"
        message+=newMess
    return message

def dateAndTime():

    beijing = timezone('Asia/Shanghai')
    beijing_time = datetime.now(beijing)
    time_now = beijing_time.strftime("%H:%M")
    print(time_now)
    if beijing_time.weekday()>4: #if the today is not a weekday
        return 1
    if (time_now >= morning_market_start and time_now <= morning_market_end) or (time_now >= afternoon_market_start and time_now <= afternoon_market_end):
        return 0 #now is in the market time
    if  time_now > morning_market_end and time_now < afternoon_market_start:
        return 2 #the noon break code
    if time_now < morning_market_start and time_now <= '08:30':
        return 3
    if time_now >afternoon_market_end:
        return 4
    return 5

def programSleep():
    #sleepcode
    #0 go for work
    #1 is weekend day sleep 9 hours
    #2 is noon break sleep 5 min
    #3 is before market sleep 1h
    #4 is after market sleep 9 hours
    #5 us 1 h before open sleep 5 m
    code1 = 32400
    code2 = 300
    code3 = 3600
    code4 = 32400
    code5 = 300
    sleepcode = dateAndTime()
    print(sleepcode)
    while sleepcode != 0:
        if sleepcode == 1:
            time.sleep(code1)
        elif sleepcode ==2:
            time.sleep(code2)
        elif sleepcode == 3:
            time.sleep(code3)
        elif sleepcode == 4:
            time.sleep(code4)
        elif sleepcode == 5:
            time.sleep(code5)
        sleepcode = dateAndTime()
    return

def crawlerDriver(url):
    sleepcode = dateAndTime()
    while sleepcode == 0:
        insertDictData(getAllStocks(url))
        print('sleeping 20mins')
        time.sleep(1200) # get new data every twenty minutes
        sleepcode = dateAndTime()
        print('finish sleeping code', sleepcode)

    return







def getHTML(url, localParam):
    try:
        r = requests.get(url, headers=headers, params=localParam)  # provide headers and parameters for the server
        # r.raise_for_status()  # detect error like 404
        html = r.content.decode()  # decode the request
        # print(type(html))
        dic = json.loads(html)  # convert str to dict
        # print(type(dic))
        listOfStock = dic["data"]["list"]  # get stock list from the dict
        for i in listOfStock:
            beijing= timezone('Asia/Shanghai')
            beijing_time = datetime.now(beijing)
            #i['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # add the time stamp
            i['time'] = beijing_time.strftime("%Y-%m-%d %H:%M:%S") #add Beijing Time to the Chinese Stock Market
        return listOfStock
    except:
        print("error: Failed to get html message")
        return

def getAllStocks(url):
    try:
        r = requests.get(url, headers=headers, params=chinese_param)  # provide headers and parameters for the server
        html = r.content.decode()  # decode the request
        dic = json.loads(html)  # convert str to dict
        count = dic["data"]["count"]  # get total number of stock
        pages = math.ceil(count / 30)  # default 30 stocks per page
        stock_list = []
        for i in range(1, pages+1):
            shenhuStockParam = {'page': i,
                                'size': '30',
                                'order': 'desc',
                                'orderby': 'percent',
                                'order_by': 'percent',
                                'market': 'CN',
                                'type': 'sh_sz',
                                '_': '1596082598401'
                                }
            local_list = getHTML(url, shenhuStockParam)
            stock_list = stock_list + local_list
            print("page:", i)
        print("Number of Stock:", len(stock_list))
        return stock_list

    except:
        print("error：Falied to get full list")
        return

if __name__ == "__main__":
    main()
