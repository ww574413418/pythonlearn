import numpy as np

A = np.arange(3,15)
print(A)

print(A[3]) #6

A = A.reshape((3,4))
print(A)
print(A[2]) # [11 12 13 14]
print(A[2][1]) # 12
print(A[2,1]) #12
# 第二行的所有数
print(A[2,:]) # [11 12 13 14]
print(A[1][1:3]) # [8 9]

# 遍历行
for row in A:
    print(row)

# 遍历列
for column in A.T:
    print(column)

# 展平
print(A.flatten())
# 遍历全部元素
for item in A.flat:
    print(item)