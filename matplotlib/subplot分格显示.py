import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspce

plt.figure(num=1)

# method1
ax1 = plt.subplot2grid((3,3),#3行3列
                       (0,0),#从(0,0)开始
                       colspan=3,#占3列
                       )
ax1.plot([1,2],[1,2])
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("ax1_title")

ax2 = plt.subplot2grid((3,3),
                       (1,0),
                       colspan=2
                       )
ax3 = plt.subplot2grid((3,3),
                       (1,2),
                       rowspan=2
                       )
ax4 = plt.subplot2grid((3,3),
                       (2,0),
                       )
ax5 = plt.subplot2grid((3,3),
                       (2,1),
                       )


plt.figure(num=2)
gs = gridspce.GridSpec(3,3) # 3行3列
ax1 = plt.subplot(gs[0,:])# 第0行,所有列:
ax2 = plt.subplot(gs[1,:2])# 第1行,前2列
ax3 = plt.subplot(gs[1:,2])#第1行到最后一行,从第2列
ax4 = plt.subplot(gs[-1,0]) #倒数第1行,第一列
ax5 = plt.subplot(gs[-1,-2]) #倒数第一行,倒数第2列

ax1.plot([0,1],[0,1])
ax1.set_title("ax1_title")
ax1.set_xlabel("x",labelpad=15)
ax1.set_ylabel("y")
#自动布局调整,防止小图和小图之间的干扰
plt.tight_layout()

# f= figure
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,#2行2列
             sharex=True,#共享x
             sharey=True#共享y
             )

ax11.scatter([1,2],[1,2])

#自动布局调整,防止小图和小图之间的干扰
plt.tight_layout()
plt.show()