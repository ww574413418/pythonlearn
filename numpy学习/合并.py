import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

# 上下合并
# [[1 1 1]
#  [2 2 2]]
C= np.vstack((A,B))
print(C)
print("A shape:{}, C shape:{}".format(A.shape,C.shape)) # A shape:(3,), C shape:(2, 3)

# 左右合并
D = np.hstack((A,B))
print(D) # [1 1 1 2 2 2]

# 竖向合并01
# 将A竖起来,给吧她的形状,从(3,) -》 (3,1)
A = A[:,np.newaxis]
print(A.shape)
print(A)
B = B[:,np.newaxis]

C = np.hstack((A,B))
# [[1 2]
#  [1 2]
#  [1 2]]
print(C)

# 竖向合并02 用这个较好
E = np.concatenate((A,B),axis=0) # 上下
print(E)
T = np.concatenate((A,B),axis=1) # 左右
print(T)

