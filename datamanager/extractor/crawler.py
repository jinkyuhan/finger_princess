from bs4 import BeautifulSoup
import requests as req
import selenium
import json
from abc import ABCMeta, abstractmethod



class Crawler(metaclass=ABCMeta):
    def __init__(self, base_url, Browser):
        self.base_url = base_url
        self.browser = Browser
        self.categories = []
        self.products = {}

    @abstractmethod
    def _move_page(self, page_num):
        pass

    @abstractmethod
    def scrap(self, category_name, category_code):
        pass

    def _add_category(self, category_name, category_code):
        for category in self.categories:
            if category_name == category['name']:
                return
        self.categories.append({
            "name": category_name,
            "code": category_code
        })
        self.products[category_name] = []

    def _add_product(self, category_name, product_info: dict):
        self.products[category_name].append(product_info)

    def get_products_in_JSON(self, category_name) -> str:
        return json.dumps(self.products[category_name], ensure_ascii=False, indent='\t')


class DanawaCrawler(Crawler):
    def __init__(self, Browser):
        super().__init__('http://prod.danawa.com/list', Browser)

    def _move_page(self, page_num):
        self.browser.execute_script('javascript:movePage({})'.format(page_num))

    # Scarp Danawa and fill the self.products
    def scrap(self, category_name, category_code):
        self._add_category(category_name, category_code)
        self.browser.move_location(self.base_url+'/?cate='+category_code)
        self.browser.select_dropdown_item('.qnt_selector','90')
        page_num = 0
        while True:
            page_num += 1
            self._move_page(page_num)
            soup = BeautifulSoup(
                self.browser.get_current_html(), 'html.parser')
            scraped_list = soup.select('.prod_main_info')
            if len(scraped_list) == 0:
                break
            for each_scraped in scraped_list:
                product_info = {}
                product_info['name'] = each_scraped.select_one(
                    '.prod_info > p > a').get_text().strip()
                product_info['price'] = each_scraped.select_one(
                    'p.price_sect > a > strong').get_text().strip()
                for spec in each_scraped.select('.view_dic'):
                    product_info[spec.get('onclick')] = spec.get_text()
                self._add_product(category_name, product_info)
            if DEBUG:
                print("Collecting data in {} : {}".format(page_num, len(self.products[category_name])))



class NaverCrawler(Crawler):
    def __init__(self, Browser):
        #padingIndex: 페이지 번호
        #pagingSize: 창 하나에 표시될 제품 수
        #productSet : 쇼핑몰 종류 eg:가격비교, 백화점/홈쇼핑 ..
        #viewType: 리스트형, 블록형
        #sort: 나열 기준
        #cat_id: 카테고리 id

        super().__init__('https://search.shopping.naver.com/search/category.nhn', Browser)
        self.current_category=''
        
    def _move_page(self, page_num):
        return self._get_page_html(page_num) 

    def _get_page_html(self,page_num):
        return req.get(self.base_url+'?pagingIndex={}&pagingSize=80&productSet=model&viewType=list&sort=rel&cat_id={}'.format(page_num,self.current_category)).text

    def _add_category(self, category_name, category_code):
        super()._add_category(category_name,category_name)
        self.current_category=category_code

    # Scarp Danawa and fill the self.products
    def scrap(self, category_name, category_code):
        self._add_category(category_name, category_code)
        page_num = 0
        while True :
            page_num+=1
            resp=self._move_page(page_num)
            soup = BeautifulSoup(
                resp, 'html.parser')
            scraped_list = soup.select('#_search_list > div.search_list.basis > ul > li')
            if len(scraped_list) == 0:
                break 
            for each_scraped in scraped_list:
                product_info = {}
                product_info['name'] = each_scraped.select_one(
                    'div.info > div > a').get_text().strip()
                #예외: page 28에 가격 출시예정 -> 아래의 CSS-selector을 활용한 접근 불가능
                try:
                    product_info['price']=each_scraped.select_one('div.info > span.price > em > span.num._price_reload').get_text().strip()
                except:
                    product_info['price']=None

                # if price_tag :
                #     product_info['price'] =price_tag.get_text().strip()
                # else :
                #     product_info['price']=''

                for spec in each_scraped.select('div.info > span.detail > a'):
                    key_value_list=spec.get('title').split(':')
                    try:
                        title=key_value_list[0].strip()
                        value=key_value_list[1].strip()
                    except:
                        continue
                    else:
                        product_info[title] = value
                self._add_product(category_name, product_info)

            if DEBUG:
                print("Collecting data in {} : {}".format(page_num, len(self.products[category_name])))

class PassmarkCrawler(Crawler):
    def __init__(self):
        super().__init__('',None)

    def _move_page(self, page_num):
        pass

    def _add_category(self, category_name, category_code):
        super()._add_category(category_name,category_code)
        self.current_category=category_code

    # Scarp Danawa and fill the self.products
    def scrap(self, category_name, category_code):
        self._add_category(category_name, category_code)
        resp=req.get(category_code)
        soup = BeautifulSoup(
            resp.text, 'html.parser')
        scraped_list = soup.select('ul.chartlist > li')
        if len(scraped_list) == 0:
            return  
        for each_scraped in scraped_list:
            product_info = {}
            product_info['name'] = each_scraped.select_one(
                'a > span.prdname').get_text().strip()
            product_info['index']=each_scraped.select_one('a > span.count').get_text().strip()
            self._add_product(category_name, product_info)
        if DEBUG:
            print("Collecting data in {} : {}".format(category_name, len(self.products[category_name])))


if __name__ != "__main__":
    DEBUG = True
