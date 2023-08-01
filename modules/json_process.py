import json
import sys
sys.path.append('../database')
import database

p = database.Postgres("postgres", 'hoangtu',
                      'HoangVanTu2102@', 'localhost', 5432, True)

# p.excute_query_update('Create table data_width_height (id int NOT NULL PRIMARY KEY, width decimal, height decimal)')
with open('../data.json') as data:
    a = data.read()
query = 'INSERT INTO data_width_height VALUES '
content = json.loads(a)
for item in content["list"]:
    query += '('+item['index']+','+item['width']+','+item['height']+'),'
    
query = query[0:len(query)-1] + ';'
p.excute_query_update(query)
