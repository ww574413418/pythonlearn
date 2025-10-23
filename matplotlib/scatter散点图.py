import numpy as np
import matplotlib.pyplot as plt

n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)

#np.arctan2(y, x) 表示点 (x, y) 相对于原点的极坐标角度 θ，返回值范围是 [-π, π]。
T = np.arctan2(y,x)

# c=T 这里 c=T 表示： 用数组 T 里的值（角度）作为每个点的颜色。
#
# Matplotlib 会根据默认的颜色映射表（colormap，比如 “viridis”）把角度数值转成不同的颜色。
plt.scatter(x,y,
            s=75,
            c=T,
            alpha=0.5#透明度
            )
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

# 隐藏ticks的值
plt.xticks(())
plt.yticks(())

plt.show()