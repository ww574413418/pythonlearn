import numpy as np
from 卷积层实现.im2col import im2col
from 卷积层实现.col2im import col2im

class Pooling:
    def __init__(self, pool_h, pool_w, stride=1, padding=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.padding = padding
        self.col = None
        self.arg_max = None
        self.x = None

    def forward(self, x):

        N, C, H, W = x.shape

        # 输出尺寸
        out_h = int((H + 2 * self.padding - self.pool_h) / self.stride + 1)
        out_w = int((W + 2 * self.padding - self.pool_w) / self.stride + 1)

        # 展开输入
        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.padding)
        col = col.reshape(-1, self.pool_h * self.pool_w)

        # 最大池化
        # 记录最大值的位置
        arg_max = np.argmax(col, axis=1)
        out = np.max(col, axis=1)

        # 恢复形状为 (N, C, out_h, out_w)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        self.x = x
        self.arg_max = arg_max
        self.col = col
        self.out_h, self.out_w = out_h, out_w

        return out

    def backward(self, dout):
        '''
        在反向传播中，我们接收到上一层传下来的梯度 dout（形状为 (N, C, out_h, out_w)）。
        我们需要将这个梯度分配回 对应的输入元素位置（也就是前向时“最大值”所在的位置）。
        即：
	        •只有前向过程中被选为最大值的那个元素，会接收到梯度；
	        •其他位置梯度为 0。
        这需要我们在前向传播时保存一个 “掩码 (mask)” 或者 “索引 (argmax)” ，来记录最大值位置。
        :param dout:
        :return:
        '''
        pool_size = self.pool_h * self.pool_w
        # (N, out_h, out_w, C)
        dout = dout.transpose(0, 2, 3, 1)
        dmax = np.zeros((dout.size, pool_size))

        # 把上层梯度传给最大值对应的那个位置
        dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()

        # 恢复维度
        dmax = dmax.reshape(-1, pool_size)

        # 将梯度还原为输入形状
        dx = col2im(dmax, self.x.shape, self.pool_h, self.pool_w, self.stride, self.padding)

        return dx