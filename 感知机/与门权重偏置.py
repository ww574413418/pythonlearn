import numpy as np

x = np.array([0,1])
# 权重
w = np.array([0.5,0.5])
# 偏移
b = -0.7

print(x * w)
print(np.sum(x*w))
print(np.sum(x*w) + b)

def AND(x1,x2):
    x = np.array([x1, x2])
    # 权重
    w = np.array([0.5, 0.5])
    # 偏移
    b = -0.7

    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1