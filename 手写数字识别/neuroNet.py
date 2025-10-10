import numpy as np
from common.functions import sigmoid
from common.functions import softmax
from common.functions import cross_entropy_error
from common.gradient import numerical_gradient
from dataset.mnist import load_mnist
import matplotlib.pyplot as plt

# 定义一个神经网络
class TwoLayerNet:
    # 初始化
    def __init__(self,input_size,hidden_size,output_size,weight_init_std = 0.01):
        # 初始化权重,注意设置的大小
        self.params = {}
        # 权重使用标准正态分布 = 平均值为 0，标准差为 1 的高斯分布。初始化
        self.params["w1"] = weight_init_std * np.random.rand(input_size,hidden_size)
        # 偏置用0初始化
        self.params["b1"] = np.zeros(hidden_size)
        self.params["w2"] = weight_init_std * np.random.rand(hidden_size,output_size)
        self.params["b2"] = np.zeros(output_size)


    # 定义学习方法
    def predic(self,x):
        # 获得权重和偏置
        w1,w2 = self.params["w1"],self.params["w2"]
        b1,b2 = self.params["b1"],self.params["b2"]

        # 输入到隐藏层
        a1 = np.dot(x,w1) + b1
        z1 = sigmoid(a1) # 进入激活函数,引入非线性
        # 隐藏层到输出层
        a2 = np.dot(z1,w2) + b2
        y = softmax(a2) # 分类一般用softmax激活函数

        return y


    # 计算损失函数 x输入数据,t正确的target
    def loss(self,x,t):
        y = self.predic(x)
        loss = cross_entropy_error(y,t)
        return loss

    # 计算预测准确率
    def accuracy(self,x,t):
        y = self.predic(x)
        # y 不是直接的类别，而是一个 概率分布矩阵,argmax将他转成预测概率取最大值的下标
        y = np.argmax(y,axis=1)
        # t 真实标签也可能是 one-hot 向量
        t = np.argmax(t,axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])

        return accuracy

    # 计算神经网络题第
    def numerical_gradient(self,x,t):
        loss_w = lambda w : self.loss(x,t)

        # 保存题第
        grads = {}
        grads["w1"] = numerical_gradient(loss_w,self.params["w1"])
        grads["b1"] = numerical_gradient(loss_w,self.params["b1"])
        grads["w2"] = numerical_gradient(loss_w,self.params["w2"])
        grads["b2"] = numerical_gradient(loss_w,self.params["b2"])

        return grads

    def gradient(self, x, t):
        # 前向传播
        W1, W2 = self.params["w1"], self.params["w2"]
        b1, b2 = self.params["b1"], self.params["b2"]

        batch_num = x.shape[0]

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        # 反向传播
        dy = (y - t) / batch_num

        grads = {}
        grads["w2"] = np.dot(z1.T, dy)
        grads["b2"] = np.sum(dy, axis=0)

        dz1 = np.dot(dy, W2.T)
        da1 = dz1 * (z1 * (1 - z1))  # sigmoid 的导数
        grads["w1"] = np.dot(x.T, da1)
        grads["b1"] = np.sum(da1, axis=0)

        return grads

# 读取训练数据和测试数据
(x_train, t_train), (x_test, t_test) =  load_mnist(normalize=True, one_hot_label = True)
# 记录损失
train_loss_list = []

# 超参数
## 学习次数
iters_num = 10000
train_size = x_train.shape[0]
## 每次训练多少数据
batch_size = 100
learning_rate = 0.1

train_acc_list = []
test_acc_list = []
# 平均每个 epoch的重复次数
iter_per_epoch = max(train_size / batch_size, 1)

# 初始化神经网络
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)


# 训练
for i in range(iters_num):

    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 计算梯度
    # grads = network.numerical_gradient(x_batch,t_batch)
    grads = network.gradient(x_batch, t_batch) # 高速版 !

    # 更新参数
    for key in ('w1', 'b1', 'w2', 'b2'):
        network.params[key] -= grads[key] * learning_rate

    # 记录学习过程
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    # 计算每个 epoch的识别精度
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
    test_acc = network.accuracy(x_test, t_test)
    train_acc_list.append(train_acc)
    test_acc_list.append(test_acc)
    print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

x = np.arange(len(train_loss_list))  # 横轴：迭代次数
y = train_loss_list                  # 纵轴：损失值

plt.plot(x, y)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.title("Training Loss Curve")
plt.show()

