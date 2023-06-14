from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

url = 'https://naver.com'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)


''' 검색창
<input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
'''

# driver.find_element(By.ID, 'query').send_keys('인공지능')
# time.sleep(2)

# driver.find_element(By.CLASS_NAME, 'search_input').send_keys('블록체인')
# time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, '[placeholder="검색어를 입력해 주세요."]').send_keys('한국')
# time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="query"]').send_keys('인공지능')
time.sleep(2)

''' 버튼태그
<button type="submit" class="btn_search" onclick="window.nclk_v2(this,&quot;sch.action&quot;)"> <span id="search-btn" class="ico_btn_search"></span> <span class="blind">검색</span> </button>
'''

# driver.find_element(By.CLASS_NAME, 'btn_search').click()
# time.sleep(2)

driver.find_element(By.ID, 'query').send_keys(Keys.ENTER)
time.sleep(2)

'''
<a role="tab" href="?where=news&amp;sm=tab_jum&amp;query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5" onclick="return goOtherCR(this,'a=tab*n.jmp&amp;r=4&amp;i=&amp;u='+urlencode(this.href));" class="tab" aria-selected="false">뉴스</a>
'''

driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[4]/a').click()
time.sleep(2)

# 현재 페이지의 뉴스 제목 가져오는 함수 만들기
def get_page_news_title():
    # HTML 코드 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    '''
    <a href="http://www.newsis.com/view/?id=NISX20230613_0002336220&amp;cID=10802&amp;pID=14000" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws*a.tit&amp;r=1&amp;i=88000127_000000000000000011909352&amp;g=003.0011909352&amp;u='+urlencode(this.href));" title="인천시, 초거대 인공지능과 지역특화산업 연계 모색">인천시, 초거대 <mark>인공지능</mark>과 지역특화산업 연계 모색</a>
    <a href="https://www.yna.co.kr/view/AKR20230612058200003?input=1195m" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws*a.tit&amp;r=6&amp;i=880000D8_000000000000000013995919&amp;g=001.0013995919&amp;u='+urlencode(this.href));" title="포스코이앤씨, 건설업계 최초 'AI+' 인공지능 인증 획득">포스코이앤씨, 건설업계 최초 'AI+' <mark>인공지능</mark> 인증 획득</a>
    '''

    news = soup.find_all('li', class_='bx')

    for n in news:
        title = n.find('a', class_='news_tit')
        if title is not None:
            result = title.get_text()
            print(result)


# 다음 페이지로 이동하는 함수 만들기
def click_next_btn():

    # 다음 페이지 이동
    driver.find_element(By.CLASS_NAME, 'btn_next').click()
    time.sleep(2)



for i in range(10):
    get_page_news_title()
    click_next_btn()