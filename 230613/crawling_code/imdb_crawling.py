import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
res = requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    
    data = soup.find('tbody', class_='lister-list')

    movies = data.find_all('tr')

    result = {}
    for movie in movies:
        title_column = movie.find('td', class_='titleColumn')
        title = title_column.find('a').get_text()
        rank = movie.find('strong').get_text()
        print(title)
        print(rank)
