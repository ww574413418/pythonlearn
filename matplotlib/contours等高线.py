import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    # the height function
    return (1-x/2 + x**5 + y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

# X,Y为网格
X,Y = np.meshgrid(x,y)

# 填充颜色
plt.contourf(X,Y,
            f(X,Y),
            8,#等高线图分几块10部分(10个圈) 0是2部分
            alpha=0.75,
            cmap=plt.cm.hot
            )
# 画等高线
C = plt.contour(X,Y,
            f(X,Y),
            8,#等高线图分几块10部分(10个圈) 0是2部分
            colors = "black",
            linewidth=0.5,
            )

plt.clabel(
    C,
    inline=True,
    fontsize = 10
)
plt.xticks(())
plt.yticks(())

plt.show()