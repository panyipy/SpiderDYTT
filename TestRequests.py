import requests
from bs4 import BeautifulSoup

passList = ["最新电影下载", "迅雷电影资源", "华语剧集专区", "欧美剧集专区", "迅雷综艺节目", "迅雷动漫资源", "游戏资源下载", "", "关于本站", "广告合作", "下载声明", "友情连接", "网站地图", "RSS订阅", "网站帮助", "滇ICP备12020060号", "网站帮助", "电影下载", "MP4电影", "经典单机游戏", "阳光电影", "最新电影"]
mainUrl = "http://www.dytt8.net/"
url = "http://www.dytt8.net"
count = 1
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
headers = {'content-type': 'application/json', 'User-Agent': userAgent}
data = requests.get(mainUrl, headers=headers).content
webdata = BeautifulSoup(data, 'lxml', from_encoding='gbk')
for link in webdata.find_all(name="a"):
    if "href" in link.attrs and link.attrs['href'] != "#":
        if link.get_text() not in passList:
            count = count + 1
            if "http" not in link.attrs['href']:
                print(url + link.attrs['href'])
            else:
                print(link.get_text() + link.attrs['href'])
print("共{}条数据".format(count))