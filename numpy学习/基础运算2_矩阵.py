import numpy as np

A = np.arange(14,2,-1).reshape((3,4))

print(A)
# 打印最小值索引
print("the index of the miniest:",A.argmin())
# 最大索引
print("the index of the maxest:",A.argmax())
# 平均值
print("the mean of the matrix:",A.mean())
print("the mean of the matrix:",np.average(A))
print("the mean of matrix row",np.mean(A,axis=0))
print("the mean of matrix column",np.mean(A,axis=1))

# 中位数
print("the median of the matrix",np.median(A))
# 累加
print("the  cumulative sum of the elements along a given axis",np.cumsum(A))
# 累差
print("Calculate the n-th discrete difference along the given axis",np.diff(A))
# 找出非0
print("find no zero",np.nonzero(A))
# 排序(逐行/逐列)
print("sroted matrix:",np.sort(A,axis=0))
# 矩阵的T
print("matrix T",A.T)
print("matrix T",np.transpose(A))
'''
如果 A 中的元素 小于 5，就把它变成 5
如果 A 中的元素 大于 9，就把它变成 9
介于 5 和 9 之间的数保持不变
'''
print("",np.clip(A,5,9))


