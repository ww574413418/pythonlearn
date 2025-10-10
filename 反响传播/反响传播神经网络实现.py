import numpy as np
from collections import OrderedDict
from Affine层 import Affine
from ReLU层 import ReLu
from SoftmaxWithLoss import SoftmaxWithLoss
from common.gradient import numerical_gradient
from 手写数字识别.dataset.mnist import load_mnist
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size,weight_init_std=0.01):
        # 初始化权重,注意权重和偏置的大小要和网络层数的大小匹配
        self.params = {}
        self.params["w1"] = weight_init_std * np.random.rand(input_size,hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["w2"] = weight_init_std * np.random.rand(hidden_size,output_size)
        self.params["b2"] = np.zeros(output_size)

        # 生成层
        self.layers = OrderedDict()
        self.layers["Affine1"] = Affine(self.params["w1"],self.params["b1"])
        self.layers["Relu1"] = ReLu()
        self.layers["Affine2"] = Affine(self.params["w2"],self.params["b2"])

        self.lastLayer = SoftmaxWithLoss()


    # 学习
    def predict(self,x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x


    # 计算损失
    def loss(self,x,t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)


    # 计算准确度
    def accuracy(self,x,t):
        y = self.predict(x)
        y = np.argmax(y,axis=1)
        if t.ndim != 1:
            t = np.argmax(t,axis=1)

        accuracy = np.sum(y==t)/float(x.shape[0])

        return accuracy



    # 计算梯度
    # 用来 检查你写的反向传播（backward）对不对
    def numerical_gradient(self, x, t):
        loss_w = lambda w : self.loss(x,t)
        grads = {}
        grads["w1"] = numerical_gradient(loss_w,self.params["w1"])
        grads["b1"] = numerical_gradient(loss_w,self.params["b1"])
        grads["w2"] = numerical_gradient(loss_w,self.params["w2"])
        grads["b2"] = numerical_gradient(loss_w,self.params["b2"])

        return grads

    # 容易写错，所以需要用 numerical_gradient 检查。
    def gradient(self, x, t):
        # forward
        self.loss(x, t)
        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)
        # 设定
        grads = {}
        grads['w1'] = self.layers['Affine1'].dw
        grads['b1'] = self.layers['Affine1'].db
        grads['w2'] = self.layers['Affine2'].dw
        grads['b2'] = self.layers['Affine2'].db

        return grads


if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) =  load_mnist(normalize=True, one_hot_label = True)
    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
    # 使用batch 的前3个来进行学习,减少时间
    x_batch = x_train[:3]
    t_batch = t_train[:3]
    grad_numerical = network.numerical_gradient(x_batch, t_batch)
    grad_backprop = network.gradient(x_batch, t_batch)
    # 求各个权重的绝对误差的平均值
    for key in grad_numerical.keys():
        diff = np.average(np.abs(grad_backprop[key] - grad_numerical[key]))
        print(key + ":" + str(diff))



