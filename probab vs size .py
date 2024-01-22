# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:44:55 2024

@author: vedan
"""
'''
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
total_iterations = 10000
invertible = 0
for i in range (1,15):
    for i in range(total_iterations):
        random_matrix = np.random.randint(2, size=(i, i))
        if np.linalg.det(random_matrix) != 0:
            invertible += 1
    probability = invertible / total_iterations
    x = i
    y = probability

plt.plot(x, y)
plt.xlabel("size of the matrix")
plt.ylabel("probability")
plt.title("probabilty vs size")
plt.show    '''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

total_iterations = 10000
sizes = list(range(1, 21))
probabilities = []

for size in sizes:
    invertible = 0

    for _ in range(total_iterations):
        random_matrix = np.random.randint(2, size=(size, size))
        
        try:
            det_value = sp.linalg.det(random_matrix)
            if not np.isinf(det_value) and det_value != 0:
                invertible += 1
        except np.linalg.LinAlgError:
            # Handling LinAlgError (e.g., singular matrix) if it occurs
            pass

    probability = invertible / total_iterations
    probabilities.append(probability)

plt.plot(sizes, probabilities, marker='o')
plt.xlabel("Size of the Matrix")
plt.ylabel("Probability")
plt.title("Probability vs Size")
plt.show()
