import numpy as np
from common.functions import cross_entropy_error
from common.functions import softmax

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None #损失
        self.y = None #softmax输出数据
        self.t = None #正确标签

    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    def backward(self,dout = 1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        return dx