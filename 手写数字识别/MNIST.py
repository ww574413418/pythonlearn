import sys,os
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

# normalize正规化为 0.0～1.0的值 flatten 图像转成一维数组 one_hot_label 标签转为one-hot 表示
(x_train,t_train),(x_test,t_test) = load_mnist(normalize=True, flatten=False, one_hot_label=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

def img_show(img):
    # 将图片转成pil格式
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


img = x_train[0]
label = t_train[0]
print(label) # 5
print(img.shape) # (784,)
img = img.reshape(28, 28) # 把图像的形状变成原来的尺寸
print(img.shape) # (28, 28)
img_show(img)