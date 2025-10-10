import numpy as np

# 一维
arr_1d = np.array([1,2,3])
# np.ndim输出数组的维度
print(np.ndim(arr_1d))
print(arr_1d.shape)
# 二维
arr_2d = np.array([[1,2],[4,5],[8,9]])
print(np.ndim(arr_2d))
print(arr_2d.shape)

# 矩阵乘法
A = np.array([[1,2],[3,4]])
print(A.shape)
B = np.array([[5,6],[7,8]])
print(B.shape)
# 矩阵乘法
print(np.dot(A,B))

A = np.array([[1,2],[3,4],[5,6]])
print(A.shape)
B = np.array([[5,6,7],[7,8,9]])
print(B.shape)
print(np.dot(A,B))