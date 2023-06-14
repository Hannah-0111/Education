import requests
from bs4 import BeautifulSoup

url = 'https://weather.com/ko-KR/weather/today/l/KSXX0037:1:KS?Goto=Redirected'
res = requests.get(url)

result = {}
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    r_data = soup.find('div', class_='TodayDetailsCard--detailsContainer--2yLtL')
    r_list = soup.find_all('div', class_='ListItem--listItem--25ojW WeatherDetailsListItem--WeatherDetailsListItem--1CnRC')
    for r in r_list:
        data = r.find('div', class_='WeatherDetailsListItem--label--2ZacS').get_text()
        temps = r.find('div', class_='WeatherDetailsListItem--wxData--kK35q').get_text()
        result[data] = temps
print(result)