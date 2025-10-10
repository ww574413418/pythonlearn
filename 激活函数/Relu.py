import numpy as np
import matplotlib.pyplot as plt
def Relu(x):
    # 输出0或者比0大的数
    return np.maximum(0,x)

x = np.arange(-5,5,1)
y = Relu(x)
plt.plot(x,y)
plt.show()