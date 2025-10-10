import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def numerical_gradient(f, x):
    #定义x_0 和 x_1的距离 x_1 = x_0 + h
    h = 1e-4 #0.0001

    # 保存梯度
    grad = np.zeros_like(x)

    for index in range(x.size):
        tmp_val = x[index]
        # 计算中心差分  [f(x+h) - f(x-h)]/2h
        # 计算f(x+h)
        x[index] = tmp_val + h
        f_x1 = f(x)
        #j计算f(x-h)
        x[index] = tmp_val - h
        f_x2 = f(x)
        grad[index] = (f_x1 - f_x2) / (2 * h)

        x[index] = tmp_val  # 还原值

    return grad

def function(x):
    if x.ndim == 1:
        return np.sum(x ** 2)
    else:
        return np.sum(x ** 2, axis=1)

