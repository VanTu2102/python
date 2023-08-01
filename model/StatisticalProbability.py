import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('../database')
import database

p = database.Postgres("postgres", 'hoangtu',
                      'HoangVanTu2102@', 'localhost', 5432, True)

# Sample data (replace this with your dataset)
data = np.array([1, 2, 4, 2.4, 5, 7, 10])

# Sort the data in ascending order
sorted_data = np.sort(data)

# Compute quantiles of the data
quantiles_data = np.percentile(sorted_data, [2, 4, 8, 4.8, 11, 14.4, 21])

# Compute quantiles from the target distribution (e.g., normal distribution)
quantiles_target = np.percentile(
    np.array([1, 2, 4, 2.4, 5, 7, 10]), [2, 4, 8, 4.8, 10, 14, 20])

# Plot the Q-Q plot
plt.scatter(quantiles_target, quantiles_data)
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.title('Q-Q Plot')
plt.show()
