import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)

y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2,linestyle="--",color="red")

# 设值坐标轴
# 显示范围
plt.xlim((-1,2))
plt.ylim((-2,3),)
# 标签
plt.xlabel("i am x")
plt.ylabel("i am y")
#
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks(
    [-2,-1.8,-1,1.23,3],
    ["really bad","bad","normal","good","really good"]
)
plt.show()