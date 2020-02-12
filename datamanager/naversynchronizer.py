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
        naver_data=[x for x in naver_data if x['price']!='']
        for laptop in naver_data:
            if 'HDD 용량' in laptop:
                if laptop['HDD 용량'] == '미포함':
                    laptop['HDD 용량']='NULL'
                elif laptop['HDD 용량'][-2:] == 'TB':
                    laptop['HDD 용량']=float(laptop['HDD 용량'][:-2])*1024
                else:
                    laptop['HDD 용량']=laptop['HDD 용량'][:-2]
            else:
                laptop['HDD 용량']='NULL'
            
            if 'SSD' in laptop:
                if laptop['SSD'][-2:] == 'TB':
                    laptop['SSD']=float(laptop['SSD'][:-2])*1024
                else:
                    laptop['SSD']=laptop['SSD'][:-2]
            else:
                laptop['SSD']='NULL'
            
            if '램' not in laptop :
                laptop['램']='NULL'
            else: 
                laptop['램']=laptop['램'].replace('GB','')

            if '해상도' not in laptop:
                laptop['해상도']='NULL'

            if '무게' not in laptop:
                laptop['무게']='NULL'

            if '화면크기' not in laptop:
                laptop['화면크기']='NULL'
            else:
                laptop['화면크기']=laptop['화면크기'][:2]

            if 'CPU' not in laptop:
                laptop['CPU']='None'

            if 'NVIDIA GPU' in laptop:
                laptop['GPU']=laptop['NVIDIA GPU']
            elif 'AMD GPU' in laptop:
                laptop['GPU']=laptop['AMD GPU']
            else:
                laptop['GPU']='None'
            if 'g' in laptop['무게']:
                laptop['무게']=float(laptop['무게'].replace('g',''))*0.001
            laptop['price']=laptop['price'].replace(',','')
        

    db = sqlite3.connect('../db.sqlite3')
    c = db.cursor()
    sql = 'DELETE FROM fp_api_laptop'
    c.execute(sql)
    db.commit()
    
    insert_sql = "INSERT OR IGNORE INTO fp_api_laptop(id,name,weight,cpu_id,gpu_id,ram,ssd,hdd,resolution,display,price) VALUES({},'{}', {}, ({}), ({}), {}, {}, {}, '{}', {}, {})"
    count = 0
    for laptop in naver_data:
        count += 1
        c.execute(insert_sql.format(count,laptop['name'],laptop['무게'],"SELECT id from fp_api_cpu where name like '%{}'".format(laptop['CPU']),"SELECT id from fp_api_gpu where name like '%{}'".format(laptop['GPU']),laptop['램'],laptop['SSD'],laptop['HDD 용량'],laptop['해상도'],laptop['화면크기'],laptop['price']))
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
