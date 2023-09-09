import sys
import numpy as np
import matplotlib.pyplot as plt
import StatisticalProbability

sys.path.append('../database')

import database;

p = database.Postgres("postgres", 'hoangtu', 'HoangVanTu2102@', 'localhost', 5432, True)

heights = []
weights = []
items = p.excute_query_get('SELECT * FROM data_height_weight')[1000:1150]
for item in items:
    heights.append(float(item[1]))
    weights.append(float(item[2]))

heights = np.array(heights)
weights = np.array(weights)
print(heights.mean())
print(weights.mean())
print(StatisticalProbability.Correlation_Coefficient(weights, heights))
plt.scatter(weights, heights)
plt.xlabel('weights')
plt.ylabel('heights')
plt.title('Plot')
plt.show()