import numpy as np
from 激活函数.sigmod import sigmoid
from common.functions import cross_entropy_error
from common.gradient import numerical_gradient
# 定义一个简单神经网络
class simpleNet:
    def __init__(self):
        #  用高斯分布进行初始化一个权重
        self.W = np.random.rand(2,3)

    def predict(self,x):
        return np.dot(x,self.W)

    def loss(self,x,t):
        z = self.predict(x)
        y = sigmoid(z)
        loss = cross_entropy_error (y,t)

        return loss


if __name__ == '__main__':

    net = simpleNet()
    print("初始权重为:")
    print(net.W)

    x = np.array([0.6,0.9])
    t = np.array([0,0,1])


    p = net.predict(x)

    print("学习结果为:",p)
    loss = net.loss(x,t)
    print("计算损失:",loss)

    # 注意 f 要与 net.W 绑定
    f = lambda W: net.loss(x, t)

    # 输出的是梯度
    dw = numerical_gradient(f,net.W)

    # 权重的梯度信息
    print(dw)