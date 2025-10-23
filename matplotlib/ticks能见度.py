import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)
y = 0.1*x
plt.figure()
plt.plot(x,y,linewidth=15,
         label="y=0.1*x",
         zorder=1#设置函数层级的优先级
        )

plt.xlim(-2,2)
ax = plt.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))


# 单独设置坐标轴ticks的label
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor="white",
                        edgecolor="None",
                        alpha=0.7,#透明度
                        ))
    label.set_zorder(10)#设置层级优先级,越大越显示在前面

plt.legend()
plt.show()

