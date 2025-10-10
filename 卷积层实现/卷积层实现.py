from im2col import im2col
from col2im import col2im
import numpy as np
class Convolution:
    def __init__(self,w,b,stride=1,padding=0):
        self.w = w
        self.b = b
        self.stride = stride
        self.padding = padding
        # 中间结果（forward 时保存，用于 backward）
        self.x = None
        self.col = None
        self.col_w = None

        # 梯度
        self.dW = None
        self.db = None


    def forward(self,x):
        '''
        Filter Number （滤波器数量）fn
        Channel c
        Filter Height fh
        Filter Width fw
        '''
        # 获取卷积核的个数,通道,长宽
        fn,c,fh,fw = self.w.shape
        # 获取输入数据的个数,通道,长宽
        n,c,h,w = x.shape
        # 计算输出数据长宽
        out_h = int((h + 2*self.padding - fh) / self.stride)
        out_w = int((w + 2*self.padding - fw) / self.stride)

        # 定义 col 获取要参与x中要参与计算的数据,并展开
        col = im2col(x,fh,fw,self.stride,self.padding)
        # 展开卷积核
        col_w = self.w.reshape(fn,-1).T
        # 计算卷积
        out = np.dot(col,col_w) + self.b
        # 将计算结果恢复成之前的4d结构 transpose(0,3,1,2) 交换位置,将之前的3换到1,1换到2,2换到3
        out = out.reshape(n,out_h,out_w,-1).transpose(0,3,1,2)

        # 保存中间变量以备反向传播
        self.x = x
        self.col = col
        self.col_w = col_w

        return out


    def backward(self,dout):
        fn,c,fh,fw = self.w.shape
        dout = dout.transpose(0, 2, 3, 1).reshape(-1, fn)

        # 计算偏置梯度
        self.db = np.sum(dout, axis=0)

        # 计算权重梯度
        self.dW = np.dot(self.col.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(fn, c, fh, fw)

        # 计算输入梯度
        dcol = np.dot(dout, self.col_W.T)
        dx = col2im(dcol, self.x.shape, fh, fw, self.stride, self.padding)

        return dx
