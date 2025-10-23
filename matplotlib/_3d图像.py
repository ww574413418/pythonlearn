import numpy as np
import matplotlib.pyplot as plt
# 处理3d的模块
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)

Z = np.sin(R)

ax.plot_surface(X,Y,Z,
                rstride=1,#用来控制绘制 3D 曲面网格的采样步长，
                cstride=1,#也就是：行（row）方向 和 列（column）方向 的采样间隔。
                cmap=plt.get_cmap("rainbow")#颜色
                )

ax.contourf(X,Y,Z,
            zdir="z",#从Z轴进行投影
            offset=-2,
            cmap="rainbow")
# 限制z轴高度
ax.set_zlim(-2,2)
plt.show()