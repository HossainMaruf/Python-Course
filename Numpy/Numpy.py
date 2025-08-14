import numpy as np

mat1 = np.array([[1,2,3], [1, 2, 3]])
mat2 = np.array([[1,2,4], [1, 2, 4], [1, 2, 3]])

print(mat1)
print(mat2)

# print(mat1 + mat2)
# print(mat1 - mat2)
# print(mat1 * mat2) 

# * and np.multiply() only for point to point multiplicatiton
# np.dot() for matrix multiplication

print(np.dot(mat1, mat2))
print(np.matmul(mat1, mat2))
print(mat1.reshape(3,3))

'''
    size()
    shape()
    reshape()
    matmul() / dot()
    multiply()
'''