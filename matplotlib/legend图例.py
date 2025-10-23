import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num=1)
# label定义图例显示的内容
l1, = plt.plot(x,y1,label="y=2x+1")
l2, = plt.plot(x,y2,color="red",linestyle="--",label="x^2")

plt.xlim((-1,2))
plt.xlabel("i am x axis")
plt.ylim((-2,3))
plt.ylabel("i am y axis")

# 显示图例 handles-处理图形 labels-自定义每个图形的名字 loc-图例的位置
plt.legend(handles=[l1,l2],labels=["aaa","bbb"],loc="best")
plt.show()
