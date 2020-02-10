from extractor.browser import Browser
from extractor.crawler import NaverCrawler
import time
import sqlite3
import json
import os

#페이지 끝까지 안돌아감.. 보통 10페이지 미만으로 작동됨

def main():
    chrome = Browser()
    naver = NaverCrawler(chrome)
    naver.scrap('laptop','50000151') #자동화 하려면 DanawaCrawler.__add_category에 구현해야함
    chrome.close()
    with open('./crawled_data/navercrawling_data.json', 'w') as f:
        f.write(naver.get_products_in_JSON('laptop'))

#db_Synchronizer 함수를 이용해서 extract된 json 형태의 데이터를 sqlite3 DB 에 넣으면 된다.

# def synchronize_with_db(): 
#     db=sqlite3.connect('./finger_princess/db.sqlite3')
#     #sqlite3 의 경우 cursor을 통해서 sql이 처리된다.
#     sql='SELECT * FROM sqlite_master WHERE type=\'table\';'
#     c=db.cursor()
#     c.execute(sql)
#     #db에 쿼리를 한 경우, 결과를 출력하기 위해 cursor.fetchall function 을 활용한다.
#     print(c.fetchall())
    
#     #cursor의 executemany() function을 활용해서 tuple형태 sqlite3에 넣는 것이 가능하다.
#     tuple_data=[('',''),('','')]
#     insert_sql='INSERT INTO Table_name(col1,col2) VALUES(%s, %s)'
#     c.executemany(insert_sql,tuple_data)



if __name__ == "__main__" :
    start_time=time.time()
    main()
    print('code execution time: ',time.time()-start_time,'secs')
    
    
   

                   