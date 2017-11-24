import requests
from bs4 import BeautifulSoup

def getData():
    url = "http://www.dytt8.net/"
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers = {'content-type': 'application/json',
               'User-Agent': userAgent}
    webData = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(webData, 'html.parser')
    movie_name = soup.select("div.co_content8 > ul > table > tbody > tr > td")
    for name in movie_name:
        data = {
            'name': name.get_text()
        }
        print(data)

getData()