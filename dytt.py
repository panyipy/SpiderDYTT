import requests
from bs4 import BeautifulSoup

url = 'http://www.dytt8.net/'
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
headers = {'content-type': 'application/json',
           'User-Agent': userAgent}
webData = requests.get(url=url, headers=headers).content.decode('gbk')
soup = BeautifulSoup(webData, 'html.parser')
movie_items_tr = soup.select("div.co_content8 > ul > table > tr > td.inddline")
# movie_items = soup.select("div.co_content8 > ul > table > tr > td.inddline > a")
count_num = 0
for items01 in movie_items_tr:
    tr_str = str(items01)
    movie_items = items01.select("a")
    if "最新电影下载" in tr_str:
        for items in movie_items:
            text = items.get_text()
            if text != "最新电影下载":
                print(text)
                string = str(items)
                a, url, content01 = string.split('"')
                url = "http://www.dytt8.net{}".format(url)
                print(url)
                count_num = count_num + 1
count_str = "共{}条数据" .format(count_num)
print(count_str)