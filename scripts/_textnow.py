#coding: utf-8

from textnow import textnow_sms
import os
import random

usernames = os.environ["TEXTNOW_USERNAME"].split(',')
passwords = os.environ["TEXTNOW_PASSWORD"].split(',')

if len(usernames) != len(passwords):
  print(u"账号和密码个数不对应")
  quit()
else:
  print(u"共有 %s 个账号，即将开始保号处理" % len(usernames))
x=random.randint(1,100)
if x<50
  numbers = '(505) 302-1529'
  msg = 'code:'+str(random.randint(100000,999999))
  for idx in range(0,len(usernames)):
    username=usernames[idx]
    password=passwords[idx]
    text = textnow_sms.Textnow(username, password, numbers, msg)
    text.send_text()
    print("---第%s个账号处理完毕---" % (idx+1))
if x>50
  numbers = '(970) 638-3082'
  msg = 'code:'+str(random.randint(100000,999999))
  for idx in range(0,len(usernames)):
    username=usernames[idx]
    password=passwords[idx]
    text = textnow_sms.Textnow(username, password, numbers, msg)
    text.send_text()
    print("---第%s个账号处理完毕---" % (idx+3))
print("---Good Job! 所有账号处理完毕---")
