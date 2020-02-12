from extractor.browser import Browser
from extractor.crawler import NaverCrawler
import time
import sqlite3
import json
import os
import sys
# 페이지 끝까지 안돌아감.. 보통 10페이지 미만으로 작동됨

def synchronize_with_db():
    naver_data = None
    with open('./crawled_data/naver_data.json', 'r') as f:
        naver_data = json.load(f)

    naver_data=[x for x in naver_data if '램' not in x and x['price'] != '']
    print(len(naver_data))

    with open('./crawled_data/wierd_data.json', 'w') as f:
        f.write(json.dumps(naver_data, ensure_ascii=False, indent='\t'))
if __name__ == "__main__":
    synchronize_with_db()