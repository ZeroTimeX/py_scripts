#coding: utf-8

from textnow import textnow_sms
import os
import random

tn = os.environ["TN"]
tn2 = os.environ["TN2"]

print(u"即将开始保号处理")
x=random.randint(1,100)
if x<50:
  numbers = '5053021529'
  msg = 'code:'+str(random.randint(100000,999999))
  text = textnow_sms.Textnow(tn, numbers, msg)
  text.send_text()
  print("---第1个账号处理完毕---")
  text = textnow_sms.Textnow(tn2, numbers, msg)
  text.send_text()
  print("---第2个账号处理完毕---")
if x>=50:
  numbers = '9706383082'
  msg = 'code:'+str(random.randint(100000,999999))
  text = textnow_sms.Textnow(tn, numbers, msg)
  text.send_text()
  print("---第1个账号处理完毕---")
  text = textnow_sms.Textnow(tn2, numbers, msg)
  text.send_text()
  print("---第2个账号处理完毕---")
print("---Good Job! 所有账号处理完毕---")
