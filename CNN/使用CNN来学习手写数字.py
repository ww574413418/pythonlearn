from 简单卷积网络 import SimpleConvNet
from 手写数字识别.dataset.mnist import load_mnist
import matplotlib.pyplot as plt
import numpy as np

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
CNN = SimpleConvNet()


# 训练
for i in range(iters_num):

    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    CNN.predict(x_batch)
    loss = CNN.loss(x_batch,t_batch)


    print(loss)




