import numpy as np

arry1 = np.array([2,4,6])
arry2 = np.array([1,2,3])

print(arry1 * arry2)
print(arry1 / 2)

# 2维数组
arry1_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix1 = np.array([[0],[0],[0]])
print(arry1_2d * 10)
print(arry1_2d.shape)
print(matrix1.shape)
print(arry1_2d * matrix1)

# 将矩阵变成一维数组
arry3 = arry1_2d.flatten()
print(arry3) # [1 2 3 4 5 6 7 8 9]
print(arry1_2d > 3)
#输出大于3的数据
print(arry1_2d[arry1_2d > 3])#[4 5 6 7 8 9]
