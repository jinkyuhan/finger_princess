from extractor.browser import Browser
from extractor.crawler import DanawaCrawler
import time
import sqlite3
import json
import os
import sys

#category code
#laptop :  '112758'
#tablet : '12210596'


def crawl():
    chrome = Browser()
    danawa = DanawaCrawler(chrome)
    danawa.scrap('laptop','112758') #자동화 하려면 DanawaCrawler.__add_category에 구현해야함
    with open('./crawled_data/danawa_data.json', 'w') as f:
        f.write(danawa.get_products_in_JSON('laptop'))
#db_Synchronizer 함수를 이용해서 extract된 json 형태의 데이터를 sqlite3 DB 에 넣으면 된다.

def synchronize_with_db():
    pass
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



if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) <2:
        print('wrong execution')
        print('Proper execution\npython naversynchronizer <option>')
        print('option types','-c : crawling only','-s : synchronizing only','-a : both',sep='\n')
    elif sys.argv[1]=='-c':
         crawl()
    elif sys.argv[1]=='-s':
        synchronize_with_db()
    elif sys.argv[1]=='-a':
        crawl()
        synchronize_with_db()
    else:
        print('wrong option')
    print('code execution time: ', time.time()-start_time, 'secs')
    
    
   

                   