import requests
from bs4 import BeautifulSoup

class DYTT():
    def __init__(self):
        self.mainUrl = 'http://www.dytt8.net/'
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        self.headers = {'content-type': 'application/json', 'User-Agent': self.userAgent}

    def getWebData(self):
        webData = requests.get(url=self.mainUrl, headers=self.headers).content.decode('gbk')
        soup = BeautifulSoup(webData, 'html.parser')
        return soup

    #获取最新电影标题和详情页面链接
    def getDetailData(self):
        soup = self.getWebData()
        movie_items_tr = soup.select("div.co_content8 > ul > table > tr > td.inddline")
        # movie_items = soup.select("div.co_content8 > ul > table > tr > td.inddline > a")
        count_num = 0
        result_dict = {}
        title_list = []
        for items01 in movie_items_tr:
            tr_str = str(items01)
            movie_items = items01.select("a")
            if "最新电影下载" in tr_str:
                for items in movie_items:
                    text = items.get_text()
                    if text != "最新电影下载":
                        string = str(items)
                        a, url, content01 = string.split('"')
                        #详情页面URL
                        url = "http://www.dytt8.net{}".format(url)
                        #电影标题
                        title = text
                        count_num = count_num + 1
                        title_list.append(title)
                        result_dict[title] = url
        result_dict['total'] = count_num
        result_dict['title_list'] = title_list
        return result_dict

    #请求对应详情页面的响应
    # def getDetailResponse(self):
    #     detail_dict = self.getDetailData()
    #     for title in detail_dict:
    #         if title != "total":
    #             url = detail_dict[title]
    #             print(url)
    #             webData = requests.get(url=url, headers=self.headers).content.decode('gbk')
    #             soup = BeautifulSoup(webData, 'html.parser')

    #通过搜索电影名获取相关信息
    def getDetailBySearch(self):
        detail_dict = self.getDetailData()
        name_list = detail_dict['title_list']
        search_name = input("请输入电影名：")
        result = ""
        for title in name_list:
            if search_name in title:
                result = title
            else:
                pass
        if result != "":
            print(result)
        else:
            print("无此电影")

a = DYTT()
a.getDetailBySearch()