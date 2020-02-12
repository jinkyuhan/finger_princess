from extractor.browser import Browser
from extractor.crawler import NaverCrawler
import time
import sqlite3
import json
import os
import sys
# 페이지 끝까지 안돌아감.. 보통 10페이지 미만으로 작동됨


def crawl():
    chrome = Browser()
    naver = NaverCrawler(chrome)
    # 자동화 하려면 DanawaCrawler.__add_category에 구현해야함
    naver.scrap('laptop', '50000151')
    chrome.close()
    with open('./crawled_data/naver_data.json', 'w') as f:
        f.write(naver.get_products_in_JSON('laptop'))

def synchronize_with_db():
    naver_data = None
    with open('./crawled_data/naver_data.json', 'r') as f:
        naver_data = json.load(f)
        
    naver_data = [x for x in naver_data if x['price'] != '' and '램' in x and '해상도' in x and '무게' in x and '화면크기' in x]
    for laptop in naver_data:
        if 'HDD 용량' in laptop:
            if laptop['HDD 용량'][-2:] == 'TB':
                laptop['HDD 용량']=laptop['HDD 용량'][:-2]*1024
            else:
                laptop['HDD 용량']=laptop['HDD 용량'][:-2]
        else:
            laptop['HDD 용량']=None
        
        if 'SSD' in laptop:
            if laptop['SSD'][-2:] == 'TB':
                laptop['SSD']=laptop['SSD'][:-2]*1024
            else:
                laptop['SSD']=laptop['SSD'][:-2]
        else:
            laptop['SSD']=None

    db = sqlite3.connect('../db.sqlite3')
    c = db.cursor()
    sql = 'DELETE FROM fp_api_laptop'
    c.execute(sql)
    db.commit()
    
    insert_sql = "INSERT OR IGNORE INTO fp_api_laptop(id,name,weight,cpu_id,gpu_id,ram,ssd,hdd,resolution,display,price) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    count = 0
    for laptop in naver_data:
        count += 1
        if 'CPU' in laptop:
            c.execute("SELECT id from fp_api_cpu where name like '%{}'".format(laptop['CPU']))
            result=c.fetchone()
            if result != None:
                laptop['CPU']=result[0]
            else:
                laptop['CPU']=None
        else:
            laptop['CPU']=None
        
        if 'NVIDIA GPU' in laptop:
            c.execute("SELECT id from fp_api_gpu where name like '%{}'".format(laptop['NVIDIA GPU']))
            result=c.fetchone()
            if result == None:
                laptop['GPU']=None
            else:
                laptop['GPU']=result[0]
        elif 'AMD GPU' in laptop:
            c.execute("SELECT id from fp_api_gpu where name like '%{}'".format(laptop['AMD GPU']))
            result=c.fetchone()
            if result == None:
                laptop['GPU']=None
            else:
                laptop['GPU']=result[0]
        else:
            laptop['GPU']=None

        c.execute(insert_sql,(count,laptop['name'],laptop['무게'],laptop['CPU'],laptop['GPU'],laptop['램'].replace('GB',''),laptop['SSD'],laptop['HDD 용량'],laptop['해상도'],laptop['화면크기'][:2],laptop['price'].replace(',','')))
    db.commit()
    c.close()


if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) < 2:
        print('wrong execution')
        print('Proper execution\npython naversynchronizer <option>')
        print('option types', '-c : crawling only',
              '-s : synchronizing only', '-a : both', sep='\n')
    elif sys.argv[1] == '-c':
        crawl()
    elif sys.argv[1] == '-s':
        synchronize_with_db()
    elif sys.argv[1] == '-a':
        crawl()
        synchronize_with_db()
    else:
        print('wrong option')
    print('code execution time: ', time.time()-start_time, 'secs')
