import matplotlib.pyplot as plt
import numpy as np

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

# gca = get current axis 得到当前坐标系
ax = plt.gca()
# 得到右边的边框,让他消失
ax.spines["right"].set_color("none")
# 得到左边的边框,让他消失
ax.spines["top"].set_color("none")
# 将x轴设置为底边边框
ax.xaxis.set_ticks_position("bottom")
# 将y轴设置成左边边框
ax.yaxis.set_ticks_position("left")
# 移动底边和左边边框
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))
plt.show()