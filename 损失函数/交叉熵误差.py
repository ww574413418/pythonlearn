import numpy as np

def  cross_entropy_error(predics,targets):
    # 当出现 np.log(0)时，np.log(0)会变为负无限大
    # 的 -inf，这样一来就会导致后续计算无法进行。作为保护性对策，添加一个
    # 微小值可以防止负无限大的发生。
    delta = 1e-7
    return -np.sum(targets * np.log(predics + delta))