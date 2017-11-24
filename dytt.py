import requests
from bs4 import BeautifulSoup

def getData():
    url = "http://www.dytt8.net/"
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers = {'content-type': 'application/json',
               'User-Agent': userAgent}
    webData = requests.get(url=url, headers=headers).content.decode('gbk')
    soup = BeautifulSoup(webData, 'html.paraser')
    #修改试试

getData()