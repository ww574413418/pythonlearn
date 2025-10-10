import numpy as np

class AdaGrad:
    def __init__(self,lr = 0.001):
        self.lr = lr
        self.h = None
        self.eps = 1e-7  # 防止除零

    def update(self,params,grads):

        if self.h is None:
            self.h = {}
            # 初始化h h是一个字典数据,由于每一个权重的矩阵可能不一样,需要每一个都单独设置
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            # 1.计算历史梯度
            self.h = self.h + grads[key] * grads[key]
            # 2. 更新梯度
            params[key] = params[key] - self.lr *  grads[key] / (np.sqrt(h) + self.eps)


