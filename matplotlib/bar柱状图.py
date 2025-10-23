import numpy as np
import matplotlib.pyplot as plt

n = 12
x = np.arange(n)
y1 = (1 - x/float(n)) * np.random.uniform(0.5,1.0,n)
y2 = (1 - x/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(x,+y1,
        facecolor="red",#柱体颜色
        edgecolor="white"#边框颜色
        )
plt.bar(x,-y2,facecolor="blue",edgecolor="white")

# 每个柱添加数值
# zip(x,y1) 将x=x,y=y1  (x,y1)只会输出一个值
for a,b in zip(x,y1):
    plt.text(a + 0.3,
             b + 0.05,
             "%.2f"%b, #展示的数值
             ha="center",# horizontal alignment 横向对齐方式
             va = "bottom" #vertical alignment 纵向对齐方式
             )

for a,b in zip(x,y2):
    plt.text(a  + 0.3,
             -b - 0.05,
             "-%.2f"%b, #展示的数值
             ha="center",# horizontal alignment 横向对齐方式
             va = "top" #vertical alignment 纵向对齐方式
             )

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()