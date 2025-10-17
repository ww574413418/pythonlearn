from 池化层实现.Pooling import Pooling
from 卷积层实现.卷积层实现 import Convolution
from collections import OrderedDict
from 反响传播.ReLU层 import ReLu as Relu
from 反响传播.SoftmaxWithLoss import SoftmaxWithLoss
from 反响传播.Affine层 import Affine
import numpy as np

class SimpleConvNet:
    def __init__(self,input_dim=(1,28,28),conv_param= {
        "filter_num" : 30,
        "filter_size" : 5,
        "stride" : 1,
        "pad" : 0
    },hidden_size = 100,output_size=10,weight_init_std=0.01):
        # 卷积个数
        filter_num = conv_param["filter_num"]
        # 卷积大小
        filter_size = conv_param["filter_size"]
        filter_stride = conv_param["stride"]
        filter_pad = conv_param["pad"]
        input_size = input_dim[1]
        # 输出的格式为(N,C,H,W) 4d
        conv_output_size = (input_size + 2 * filter_pad - filter_size)/filter_stride + 1
        # 计算affine层的大小 2d (n,d)
        # 经过卷积层(n,1,28,28) 经过pool (n,1,14,14) 之后转成(n,1*14*14) 这里假设通道为1
        pool_output_size = int(filter_num * (conv_output_size / 2) * (conv_output_size / 2))
        self.params = {}

        # 定义权重
        self.params["W1"] = weight_init_std * np.random.randn(filter_num, input_dim[0],filter_size, filter_size)
        self.params['b1'] = np.zeros(filter_num)
        self.params['W2'] = weight_init_std * np.random.randn(pool_output_size, hidden_size)
        self.params['b2'] = np.zeros(hidden_size)
        self.params['W3'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b3'] = np.zeros(output_size)

        # 定义神经网络
        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution(self.params['W1'],
                                           self.params['b1'],
                                           conv_param['stride'],
                                           conv_param['pad'])
        self.layers['Relu1'] = Relu()
        self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
        self.layers['Affine1'] = Affine(self.params['W2'],
                                        self.params['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W3'],
                                        self.params['b3'])
        self.last_layer = SoftmaxWithLoss()

    def predict(self, x):
        # 如果输入是二维（展平的），则恢复为4D
        if x.ndim == 2:
            x = x.reshape(x.shape[0], 1, 28, 28)
        for layer in self.layers.values():
            x = layer.forward(x)
        return x

    def loss(self, x, t):
        y = self.predict(x)
        return self.last_layer.forward(y, t)
