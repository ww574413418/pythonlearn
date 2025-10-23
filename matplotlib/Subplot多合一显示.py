import numpy as np
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,1,1)#分成2行1列,第1个位置
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)#分成2行3列,第1个位置
plt.plot([0,1],[0,1])

plt.subplot(2,3,5)#分成2行3列,第2个位置
plt.plot([0,1],[0,1])

plt.subplot(2,3,6)#分成2行3列,第3个位置
plt.plot([0,1],[0,1])

plt.show()