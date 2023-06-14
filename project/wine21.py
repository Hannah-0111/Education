import requests
from bs4 import BeautifulSoup
import urllib

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

url = 'https://www.wine21.com/13_search/monthly_list.html'
res = requests.get(url)

result = {}
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    box = soup.find('div', class_='board-list-wine')
    thumb = box.find_all('div', class_='thumb')
    for idx, parts in enumerate(thumb):
        part = parts.find('img')['src']
        label = parts.find('img')['alt']
        result[idx] = label
        urllib.request.urlretrieve(part, f'./img/{idx}.png')
    print('success')
    print(result)
else:
    print('fail')



