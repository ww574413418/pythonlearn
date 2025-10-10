import numpy as np

#predics的格式为(batcsize,predict)
def  cross_entropy_error(predicts,targets):
    # 当出现 np.log(0)时，np.log(0)会变为负无限大
    # 的 -inf，这样一来就会导致后续计算无法进行。作为保护性对策，添加一个
    # 微小值可以防止负无限大的发生。

    if np.ndim(predicts) == 1: #(,predict)
        predics = np.reshape(1,predicts) # 转成(1,predict)
        targets = np.reshape(1,targets)
    # 拿到batchsize大小
    batch_size = predicts.shape[0]

    delta = 1e-7
    return -np.sum(targets * np.log(predicts + delta)) / batch_size

    #此外，当监督数据是标签形式（非 one-hot 表示，而是像“2”“7”这样的标签）时，交叉熵误差可通过如下代码实现
    # predicts[0, 1] → 取第0行、第1列
    # predicts[1, 0] → 取第1行、第0列
    # predicts[2, 2] → 取第2行、第2列
    # return -np.sum(np.log(predicts[np.arange(batch_size),targets]  + delta)) / batch_size

