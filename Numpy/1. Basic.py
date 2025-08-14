import numpy as np
matA = np.array([[1, 2, 3], [3, 4, 5]])
matB = np.array([[2, 3], [3, 4], [4, 5]])
print(np.shape(matA), np.shape(matB))
result = np.dot(matA, matB)
invert_result = np.linalg.inv(result)
identity = np.matmul(result, invert_result)
print(identity)
