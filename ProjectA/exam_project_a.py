from bs4 import BeautifulSoup
import requests
import pandas as pd


class Project_A:
    def __init__(self):
        pass

    def get_soup(self, url):
        html_doc = requests.get(url).content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def get_page_size(self, soup):
        return soup.select('.pagenation-box')[0]['data-pages']

    def get_data(self, soup):
        raw = soup.select(
            '.search-result-list')[0].find_all(class_='search-result-list-item')
        data = []
        for r in raw:
            car_info = {}
            car_info['name'] = r.a.select('.cx-name')[0].get_text()
            price = r.a.select('.cx-price')[0].get_text()
            if price != '暂无':
                car_info['price_low'], car_info['price_high'] = price[:-1].split('-')
            else:
                car_info['price_low'], car_info['price_high'] = price, price
            car_info['img_url'] = r.a.img['src']
            # print(car_info)
            data.append(car_info)
        return data

    def write_to_csv(self, data):
        dataframe = pd.DataFrame(data)
        # print(dataframe)
        dataframe.to_csv('data.csv', index=False)

    def run(self):
        page = '1'
        base_url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8&page='
        url = base_url + page
        first_page = self.get_soup(url)
        page_size = self.get_page_size(first_page)
        data = self.get_data(first_page)
        # print(page_size)
        if page_size == '1':
            '''
            write to csv
            '''
            pass
        else:
            for i in range(page_size):
                if i != 0:
                    another_page = self.get_soup(base_url+str(i+1))
                    another_page_data = self.get_data(another_page)
                    data.append(another_page_data)
        self.write_to_csv(data)


if __name__ == "__main__":
    project = Project_A()
    project.run()
