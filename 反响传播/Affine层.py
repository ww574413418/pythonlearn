import numpy as np

class Affine:

    def __init__(self,w,b):
        self.w = w #权重
        self.b = b #偏置
        self.x = None
        self.dx = None
        self.dw = None
        self.db = None

    def forward(self,x):
        self.x = x
        return np.dot(x,self.w) + self.b

    def backward(self,dout):
        # dx = dy*wT
        dx = np.dot(dout,self.w.T)
        # dw = xT*dy
        dw = np.dot(self.x.T,dout)
        db = np.sum(dout,axis=0)
        self.dx = dx
        self.dw = dw
        self.db = db
        return dx

