#!/usr/bin/env python3   #可以直接在Unix/Liux/Mac上运行
# -*- coding: utf-8 -*-   #使用UTF-8编码

' a test module'          #模块的文档注释

_author_ = 'Wei Tang'     #变量的作者

from wxpy import *

import time
print("本软件采用特殊字符检测，即对方收不到任何信息！")
print("或许某个版本微信就会修复该字符了，不作通知哈！")
print("软件编写日期：2019-2-20！")
input("任意键继续...(非电源键)")
try:
    bot = Bot()#机器人对象
    all_friends = bot.friends()#把微信所有好友放进列表
    for i in all_friends:
        try:
            print("检测 "+i.name+" 中...")#如果好友备注有表情这句会报错，所以报错直接跳过
        except:
            pass
        try:
            i.send('జ్ఞ ‌ా')#发送检测字符
        except: 
            pass
        time.sleep(2) #延时防频繁
    bot.file_helper.send('检测结束，请退出网页微信!')#通过文件传输助手发送检测结束
    bot.logout()

    input("检测结束，任意键退出...")
except KeyError:#这个错误是因为微信官方封禁了这个微信号登陆网页微信的接口
    print("该微信暂时不能登录网页微信！")
    input("检测失败，任意键退出...")
 #测试同步