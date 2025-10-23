import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y1 = 0.05* x**2
y2 = -1 * y1


fig,ax1 = plt.subplots()

# ax2是ax1的反转
ax2 = ax1.twinx()

ax1.plot(x,y1,color="green")
ax1.set_xlabel("x")
ax1.set_ylabel("x")
# 添加函数标注（不是标点，而是整条线的函数表达式）
ax1.text(6, 0.05 * 6**2 + 2,     # 位置：在曲线上方一点
         r"$y=0.05x^2$",
         color="green",
         fontsize=14)

ax2.text(6, -0.05 * 6**2 - 2,    # 位置：在曲线下方一点
         r"$y=-0.05x^2$",
         color="blue",
         fontsize=14)


ax2.plot(x,y2,color="blue")
ax2.set_xlabel("x")
ax2.set_ylabel("x")



plt.show()