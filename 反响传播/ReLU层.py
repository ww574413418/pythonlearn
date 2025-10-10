import numpy as np

class ReLu:

    #这个变量 mask是由 True/False构成的 NumPy 数
    #组，它会把正向传播时的输入 x的元素中小于等于 0 的地方保存为 True，其
    #他地方（大于 0 的元素）保存为 False。
    def __init__(self):
        self.mask = None

    def forward(self,x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self,dout):
        dx = dout.copy()
        dx[self.mask] = 0
        return dx