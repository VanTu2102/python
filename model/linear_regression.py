import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('../database')

import database;

p = database.Postgres("postgres", 'hoangtu', 'HoangVanTu2102@', 'localhost', 5432, True)