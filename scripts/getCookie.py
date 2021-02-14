
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import random
import json
import requests

import importlib,sys
importlib.reload(sys)


TN_USER = '自己用户名'
TN_PASS = '自己的密码'
#在100秒内登录，否则Cookie获取错误

url = "https://www.textnow.com/login"
options = webdriver.FirefoxOptions()
#options.add_argument('-headless')  # 无头参数
driver = webdriver.Firefox(executable_path='geckodriver', options=options)

try:
    driver.get(url)
except:
    pass
time.sleep(8)
# 分辨率 1920*1080
#driver.set_window_size(1920,1080)
#presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
#visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。

WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
uname_box = driver.find_element_by_xpath("//input[@name='username']")
pass_box = driver.find_element_by_xpath("//input[@name='password']")
uname_box.send_keys(TN_USER)
pass_box.send_keys(TN_PASS)

login_btn = driver.find_element_by_xpath("//button[@type='submit']")
login_btn.click()

time.sleep(100)
cookie = driver.get_cookies() # 获取浏览器cookies
driver.quit()
print(cookie)
jsonCookies = json.dumps(cookie)
with open('tn11.json', 'w',encoding='utf-8') as f:
  f.write(jsonCookies)
















