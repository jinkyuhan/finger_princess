import pandas as pd
import time
import sqlite3

def synchronize_with_db():
    game_data=pd.read_csv('./crawled_data/recgame_data.csv',sep=',')

    game_data['game_name']=game_data['game_name'].apply(lambda x : x.replace("'s",''))
    game_data['intel_cpu']=game_data['intel_cpu'].apply(lambda x : x.lower().replace('-','').replace(' ','').replace('intel',''))
    game_data['amd_cpu']=game_data['amd_cpu'].apply(lambda x: x.lower().replace('-','').replace(' ','').replace('amd',''))
    game_data['ram']=game_data['ram'].apply(lambda x: x.replace('GB',''))
    game_data['nvidia_gpu']=game_data['nvidia_gpu'].apply(lambda x:x.lower().replace(' ','').replace('nvidia',''))
    game_data['amd_gpu']=game_data['amd_gpu'].apply(lambda x: x.lower().replace(' ','').replace('amd',''))
    game_data['storage']=game_data['storage'].apply(lambda x: x.replace('GB',''))
    game_data['vram']=game_data['vram'].apply(lambda x: x.replace('GB','').replace('None','NULL'))

    db=sqlite3.connect('../db.sqlite3')
    c=db.cursor()
    sql="DELETE FROM fp_api_game"
    c.execute(sql)
    sql="INSERT OR IGNORE INTO fp_api_game(id,name,min_ram,min_gpuram,min_storage,min_cpu_itl_id,min_cpu_amd_id,min_gpu_itl_id,min_gpu_amd_id) VALUES({},'{}',{},{},{},(SELECT id from fp_api_cpu where name like '%{}'),(SELECT id from fp_api_cpu where name like '%{}'),(SELECT id from fp_api_gpu where name like '%{}'),(SELECT id from fp_api_gpu where name like '%{}'))"

    for index in range(len(game_data)):
        c.execute(sql.format(index+1,game_data['game_name'][index],game_data['ram'][index],game_data['vram'][index],game_data['storage'][index],game_data['intel_cpu'][index],game_data['amd_cpu'][index],game_data['nvidia_gpu'][index],game_data['amd_gpu'][index]))
    db.commit()
    c.close()

if __name__ == "__main__":
    start_time = time.time()
    synchronize_with_db()
    print('code execution time: ', time.time()-start_time, 'secs')