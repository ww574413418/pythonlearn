import numpy as np
from 损失函数.梯度 import numerical_gradient
from 损失函数.梯度 import function

# lr 学习率 step_num 一共学习多少次 f 损失函数
def gradient_descent(f,init_x,lr=0.001,step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad

    return x


x = gradient_descent(function,np.array([-3.0,4.0]),lr=0.1)
print(x)