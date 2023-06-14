from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import os
import pyperclip

url = 'https://naver.com'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

'''
<a href="https://nid.naver.com/nidlogin.login?mode=form&amp;url=https://www.naver.com/" class="MyView-module__link_login___HpHMW"><i class="MyView-module__naver_logo____Y442"><span class="blind">NAVER</span></i>로그인</a>
'''

driver.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW').click()
time.sleep(2)

'''
<input type="text" id="id" name="id" placeholder="아이디" title="아이디" class="input_text" maxlength="41" value="">
'''
naver_id = 'yournaverid'
# driver.find_element(By.ID, 'id').send_keys(naver_id)
# time.sleep(2)

id_input = driver.find_element(By.ID, 'id')
pyperclip.copy(naver_id) # ctrl+c
id_input.click()
id_input.send_keys(Keys.CONTROL, 'v') # ctrl+v
time.sleep(2)

'''
<input type="password" id="pw" name="pw" placeholder="비밀번호" title="비밀번호" class="input_text" maxlength="16">
'''
naver_pw = 'naverpw'
# driver.find_element(By.ID, 'pw').send_keys(naver_pw)
# time.sleep(2)


pw_input = driver.find_element(By.ID, 'pw')
pyperclip.copy(naver_pw)
pw_input.click()
pw_input.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

'''
<button type="submit" class="btn_login" id="log.login">
<span class="btn_text">로그인</span></button>
'''

driver.find_element(By.CLASS_NAME, 'btn_login').click()
time.sleep(2)

# failed due to capcha