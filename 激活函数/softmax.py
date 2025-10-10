import numpy as np

def softmax(x):
    c = np.max(x)
    # 计算exp(a)
    exp_a = np.exp(x - c)
    # 求和exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y