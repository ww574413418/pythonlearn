import numpy as np
from 激活函数.sigmod import sigmoid,identity_function

# 输入层
## 偏移
B1 = np.array([0.1,0.2,0.3])
## 输入
x = np.array([1,5])
## 权重
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
## 计算
A1 = np.dot(x,W1) + B1
## 通过激活函数
Z1 = sigmoid(A1)

print(Z1)

# 第二层
## 偏置
B2 = np.array([0.1,0.2])
## 权重
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
## 计算
A2 = np.dot(Z1,W2) + B2
## 通过激活函数
Z2 = sigmoid(A2)

print(Z2)

# 输出层
## 偏置
B3 = np.array([0.1,0.2])
## 权重
W2 = np.array([[0.1,0.3],[0.2,0.4]])
## 计算
A3 = np.dot(Z2,W2) + B3
## 通过激活函数
Z3 = sigmoid(A3)

print(Z3)

print("---------------------------------")
# 定义神经网络
def netwokr():
    network = {}
    network["W1"] =  np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network["W2"] =  np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network["W3"] =  np.array([[0.1,0.3],[0.2,0.4]])
    network["B1"] =  np.array([0.1,0.2,0.3])
    network["B2"] =  np.array([0.1,0.2])
    network["B3"] =  np.array([0.1,0.2])

    return network

#模拟forward
def forward(network,x):
    W1,W2,W3 = network["W1"],network["W2"],network["W3"]
    B1,B2,B3 = network["B1"],network["B2"],network["B3"]

    a1 = np.dot(x,W1) + B1
    z1 = sigmoid(a1)

    a2 = np.dot(z1,W2) + B2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + B3

    y = identity_function(a3)

    return y


network = netwokr()
x = np.array([1,5])
y = forward(network,x)
print(y)

