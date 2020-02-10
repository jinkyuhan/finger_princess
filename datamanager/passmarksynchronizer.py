from extractor.crawler import PassmarkCrawler
import time
import sqlite3
import json
import os

# 페이지 끝까지 안돌아감.. 보통 10페이지 미만으로 작동됨


def crawl():
    passmark = PassmarkCrawler()
    passmark.scrap(
        'gpu', 'https://www.videocardbenchmark.net/high_end_gpus.html')
    passmark.scrap('cpu', 'https://www.cpubenchmark.net/high_end_cpus.html')
    passmark.scrap('cpu', 'https://www.cpubenchmark.net/laptop.html')
    with open('./crawled_data/gpucrawling_data.json', 'w') as f:
        f.write(passmark.get_products_in_JSON('gpu'))
    with open('./crawled_data/cpucrawling_data.json', 'w') as f:
        f.write(passmark.get_products_in_JSON('cpu'))


def synchronize_with_db():
    cpu_data=None
    gpu_data=None
    with open('./crawled_data/gpucrawling_data.json', 'r') as f:
        gpu_data=json.load(f)
    with open('./crawled_data/cpucrawling_data.json', 'r') as f:
        cpu_data=json.load(f)

    cpu_data = [{'name':x['name'],'index':x['index'].replace(',','')} for x in cpu_data if x['index'] != 'NA']
    gpu_data = [{'name':x['name'],'index':x['index'].replace(',','')} for x in gpu_data if x['index'] != 'NA']

    db=sqlite3.connect('../db.sqlite3')
    # sqlite3 의 경우 cursor을 통해서 sql이 처리된다.
    sql='SELECT * FROM sqlite_master WHERE type=\'table\';'
    c=db.cursor()
    # c.execute(sql)
    # #db에 쿼리를 한 경우, 결과를 출력하기 위해 cursor.fetchall function 을 활용한다.
    # print(c.fetchall())
    
    # cursor의 executemany() function을 활용해서 tuple형태 sqlite3에 넣는 것이 가능하다
    insert_sql='INSERT OR IGNORE INTO fp_api_cpu(name,point) VALUES(?, ?)'
    for cpu in cpu_data:
        c.execute(insert_sql,(cpu['name'],float(cpu['index'])))
    insert_sql='INSERT OR IGNORE INTO fp_api_gpu(name,point) VALUES(?, ?)'
    for gpu in gpu_data:
        c.execute(insert_sql,(gpu['name'],float(gpu['index'])))
    db.commit()
    c.close()
    



if __name__ == "__main__" :
    start_time=time.time()
    #crawl()
    synchronize_with_db()
    db=sqlite3.connect('../db.sqlite3')
    sql='SELECT * FROM fp_api_cpu;'
    c=db.cursor()
    c.execute(sql)
    # #db에 쿼리를 한 경우, 결과를 출력하기 위해 cursor.fetchall function 을 활용한다.
    print(c.fetchall())
    print('code execution time: ',time.time()-start_time,'secs')
    
    
   

                   
