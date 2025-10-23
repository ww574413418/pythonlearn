import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)

# ax.plot() 的返回值是一个 列表（list-like）,单独解包“,”,
# 相当于 line = ax.plot(x, np.sin(x))[0]
line, = ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10) )
    return line,

def init():
    line.set_ydata(np.sin(x) )
    return line,

# 动画
ani = animation.FuncAnimation(
    fig = fig,
    func= animate, # 每一帧（frame）绘制时都会调用的函数。
    init_func= init, # 动画开始前绘制背景或初始状态。
    frames=100,  # 总帧数（即动画播放的迭代次数）
    interval=20, # 每帧之间的间隔时间
    blit=True # 更新变化的点true/更新全部点false
)
plt.show()