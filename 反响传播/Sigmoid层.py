import numpy as np

class sigmoid:

    def __init__(self):
        # 保存forward的值,方便backward的时候拿取
        self.out = None

    def forward(self,x):
        out = 1 /( 1 + np.exp(-x))
        self.out = out
        return out

    def backward(self,dout):
        dy = dout * self.out * (1.0 - self.out)
        return dy