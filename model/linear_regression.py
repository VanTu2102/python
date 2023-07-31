import sys
sys.path.append('../database')

import database;

p = database.Postgres("postgres", 'hoangtu', 'HoangVanTu2102@', 'localhost', 5432, True)