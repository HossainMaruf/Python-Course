# 2D List (Matrix) indexing and slicing
# List of List

import numpy as np


matA = np.array([[1, 2, 3], [3, 4, 10], [30,12, 5]])
index = np.shape(matA)[0] - 1
sum = 0

for row in matA:
    sum = sum + row[index]
    index = index-1

print(sum)
