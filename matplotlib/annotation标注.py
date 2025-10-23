import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x + 1

plt.figure()
plt.plot(x,y)

ax = plt.gca()
# 清楚 顶部和右边的边框
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# 将左边和底边设置成y,x轴
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

# 移动左边和底边
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))


# 添加一个点
x_0 = 1
y_0 = 2*x_0 + 1
plt.scatter(x_0,y_0,s=50,color="y")

#画坐标线
plt.plot([x_0,x_0],[y_0,0],color="red",linestyle="--",linewidth=2)

# 添加annotation 标注
plt.annotate(
    r"$2x+1%s$"%y_0,
    xy=(x_0,y_0),
    xycoords="data", # 告诉 Matplotlib xy 是用的数据坐标。
    xytext=(+30,-30), # 标注文字的位置，相对箭头指向的点进行偏移
    textcoords="offset points", # 设置上面 xytext 的坐标系统
    fontsize=16,
    arrowprops=dict(
        arrowstyle = "->",#剪头格式
        connectionstyle="arc3,rad=.2"#rad 是弧度，正值表示顺时针弯，负值表示逆时针弯。
    )
)
# 使用test来添加标注
plt.text(-3,3,r"this is a test",fontdict={"size":12})
plt.show()