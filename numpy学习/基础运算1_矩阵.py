import numpy as np

a = np.array([10,20,30,40])
# 0 1 2 3
b = np.arange(4)

c = a - b # [10 19 28 37]
c = a + b # [10 21 32 43]
c = b**2 # [0 1 4 9]

c = 10*np.sin(a) # [-5.44021111  9.12945251 -9.88031624  7.4511316 ]
c = 10*np.cos(a) # [-8.39071529  4.08082062  1.5425145  -6.66938062]

print(c)

print(b < 3) # [ True  True  True False]
print(b == 3) # [False False False  True]

a = np.array([[1,1],[0,1]])
b = b.reshape((2,2))

# 对应位置相乘
c = a * b
# 矩阵乘法
c = np.dot(a,b)
print(c)

# 创建随机矩阵(每个数都在0~1之间)
a = np.random.random((2,4))

sum = np.sum(a)
min = np.min(a)
max = np.max(a)

print("sum:{}, min:{}, max:{}".format(sum,min,max))

# axis=1 列, axis=0 行
sum = np.sum(a,axis=1)
min = np.min(a,axis=1)
max = np.max(a,axis=1)

print("sum:{}, min:{}, max:{}".format(sum,min,max))

sum = np.sum(a,axis=0)
min = np.min(a,axis=0)
max = np.max(a,axis=0)

print("sum:{}, min:{}, max:{}".format(sum,min,max))