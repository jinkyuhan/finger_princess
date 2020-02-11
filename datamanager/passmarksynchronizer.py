from extractor.crawler import PassmarkCrawler
import time
import sqlite3
import json
import os
import sys

# 페이지 끝까지 안돌아감.. 보통 10페이지 미만으로 작동됨


def crawl():
    passmark = PassmarkCrawler()
    passmark.scrap(
        'gpu', 'https://www.videocardbenchmark.net/high_end_gpus.html')
    passmark.scrap('cpu', 'https://www.cpubenchmark.net/high_end_cpus.html')
    passmark.scrap('cpu', 'https://www.cpubenchmark.net/laptop.html')
    with open('./crawled_data/gpu_data.json', 'w') as f:
        f.write(passmark.get_products_in_JSON('gpu'))
    with open('./crawled_data/cpu_data.json', 'w') as f:
        f.write(passmark.get_products_in_JSON('cpu'))


def synchronize_with_db():
    cpu_data=None
    gpu_data=None
    with open('./crawled_data/gpu_data.json', 'r') as f:
        gpu_data=json.load(f)
    with open('./crawled_data/cpu_data.json', 'r') as f:
        cpu_data=json.load(f)

    cpu_data = [{'name':x['name'],'index':x['index'].replace(',','')} for x in cpu_data if x['index'] != 'NA']
    gpu_data = [{'name':x['name'],'index':x['index'].replace(',','')} for x in gpu_data if x['index'] != 'NA']

    db=sqlite3.connect('../db.sqlite3')
    # sqlite3 의 경우 cursor을 통해서 sql이 처리된다.
    
    c=db.cursor()
    sql='DELETE FROM {}'
    c.execute(sql.format('fp_api_cpu'))
    c.execute(sql.format('fp_api_gpu'))
    db.commit()

    insert_sql='INSERT OR IGNORE INTO {}(id,name,point) VALUES(?, ?, ?)'
    count=0
    for cpu in cpu_data:
        count+=1
        c.execute(insert_sql.format('fp_api_cpu'),(count,cpu['name'],float(cpu['index'])))
    count=0
    for gpu in gpu_data:
        count+=1
        c.execute(insert_sql.format('fp_api_gpu'),(count,gpu['name'],float(gpu['index'])))
    db.commit()
    c.close()
    

if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) <2:
        print('wrong execution')
        print('Proper execution\npython passmarksynchronizer <option>')
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