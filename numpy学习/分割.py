import numpy as np

A = np.arange(12).reshape(3,4)
print(A)

# 横向分割 3 行 每个分割必须相等
# [array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])]
print(np.split(A,1,axis=0))

# 纵向分割 2列 每个分割必须相等
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]
print(np.split(A,2,axis=1))

# 不等分割
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2],
#        [ 6],
#        [10]]), array([[ 3],
#        [ 7],
#        [11]])]
print(np.array_split(A,3,axis=1))

# 纵向分割
print(np.vsplit(A,3))

# 横向分割
print(np.hsplit(A,2))