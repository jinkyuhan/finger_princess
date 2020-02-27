import pandas as pd
import time
import sqlite3

def synchronize_with_db():
    game_data=pd.read_csv('./crawled_data/program_data.csv',sep=',')

    game_data['program_name']=game_data['name']
    game_data['cpu']=game_data['cpu'].apply(lambda x : x.lower().replace('-','').replace(' ',''))
    game_data['gpu']=game_data['gpu'].apply(lambda x: x.lower().replace(' ',''))
    game_data['ram']=game_data['ram']

    db=sqlite3.connect('../db.sqlite3')
    c=db.cursor()
    sql="DELETE FROM fp_api_program"
    c.execute(sql)
    sql="INSERT OR IGNORE INTO fp_api_program(id,name,rec_ram,rec_cpu_id,rec_gpu_id) VALUES({},'{}',{},(SELECT id from fp_api_cpu where name like '%{}'),(SELECT id from fp_api_gpu where name like '%{}'))"

    for index in range(len(game_data)):
        c.execute(sql.format(index+1,game_data['program_name'][index],game_data['ram'][index],game_data['cpu'][index],game_data['gpu'][index]))
    db.commit()
    c.close()

if __name__ == "__main__":
    start_time = time.time()
    synchronize_with_db()
    print('code execution time: ', time.time()-start_time, 'secs')