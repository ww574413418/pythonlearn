import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,2,4,2,5,8,7]

# 定义大图的大小和位置
left,bottom,width,height = 0.1,0.1,0.8,0.8

ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,color="red")
ax1.set_title("ax1_title")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

# 法一、
# 定义小图的大小和位置
left,bottom,width,height = 0.2,0.6,0.25,0.25

ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,color="blue")
ax2.set_title("ax2_title")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# 法二、
plt.axes([0.6,0.2,0.25,0.25])
plt.plot(y[::-1],x,color="green")
plt.title("ax3_title")
plt.xlabel("x")
plt.ylabel("y")

plt.show()