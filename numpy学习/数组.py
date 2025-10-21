import numpy as np

# 把数字定义维数组
array = np.array([[2,4,6],[7,8,9]],dtype=int)


# 数组的属性
# 维度
print("array`s dim:",array.ndim)
# 形状
print("array`s shape:",array.shape)
# 大小
print("array`s size:",array.size)
# 类型
print("array`s type:",array.dtype)

# 定义全0矩阵
zero_matrix = np.zeros((3,3))

print("zero matrix:",zero_matrix)

# 定义全是1的矩阵
ones_matrix = np.ones((3,3))

print("ones matrix:",ones_matrix)

# 定义一个空矩阵
empty_matrix = np.empty((3,3))
print("empty matrix",empty_matrix)

# 生成有序的数组(开始,结束,步幅)
sorted_array = np.arange(0,10,2)
print("sorted array:",sorted_array)

# 重新定义形状
sorted_array2 = np.arange(12).reshape((3,4))
print("sorted array2:",sorted_array2)

# 生成等差数列(开始,结束,步幅)
A_P_array = np.linspace(1,10,5)
print("​arithmetic progression",A_P_array)

