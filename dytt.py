import requests
from bs4 import BeautifulSoup

url = 'http://www.dytt8.net/'
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
headers = {'content-type': 'application/json',
           'User-Agent': userAgent}
webData = requests.get(url=url, headers=headers).content.decode('gbk')
soup = BeautifulSoup(webData, 'html.parser')
items_dict = {}
movie_items = soup.select("div.co_content8 > ul > table > tr > td.inddline > a")
for items in movie_items:
    text = items.get_text()
    if text != "最新电影下载":
        print(text)
        string = str(items)
        a, url, content01 = string.split('"')
        url = "http://www.dytt8.net{}".format(url)
        print(url)