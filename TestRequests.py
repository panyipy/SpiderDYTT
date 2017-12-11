import requests
from bs4 import BeautifulSoup

class DYTT():
    def __init__(self):
        self.mainUrl = 'http://www.dytt8.net/'
        self.url = "http://www.dytt8.net"
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        self.headers = {'content-type': 'application/json', 'User-Agent': self.userAgent}
        self.passList = ["最新电影下载", "迅雷电影资源", "华语剧集专区", "欧美剧集专区", "迅雷综艺节目", "迅雷动漫资源", "游戏资源下载", "", "关于本站", "广告合作", "下载声明", "友情连接", "网站地图", "RSS订阅", "网站帮助", "滇ICP备12020060号", "网站帮助", "电影下载", "MP4电影", "经典单机游戏", "阳光电影", "最新电影"]

    def getWebData(self):
        webData = requests.get(url=self.mainUrl, headers=self.headers).content.decode('gbk')
        soup = BeautifulSoup(webData, 'lxml', from_encoding='gbk')
        return soup

    def getTilAndUrl(self):
        content = {}
        count = 1
        webdata = self.getWebData()
        for link in webdata.find_all(name="a"):
            if "href" in link.attrs and link.attrs['href'] != "#":
                if link.get_text() not in self.passList:
                    count = count + 1
                    if "http" not in link.attrs['href']:
                        content[link.get_text()] = self.url + link.attrs['href']
                    else:
                        content[link.get_text()] = link.attrs['href']
        content["count"] = count
        return content

    def showNameList(self):
        content = self.getTilAndUrl()
        for name in content:
            print(name)

    def searchName(self):
        self.showNameList()
        content_index = "无此电影！"
        content = self.getTilAndUrl()
        search_name = input("请输入电影名：")
        for movies in content:
            if search_name in movies:
                content_index = movies
                break
            else:
                pass
        if content_index != "无此电影！":
            print(content_index)
            print(content[content_index])
        else:
            print(content_index)
            self.searchName()

a = DYTT()
a.searchName()