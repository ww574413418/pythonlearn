import numpy as np
import matplotlib.pyplot as plt

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)


plt.imshow(a,
           interpolation="nearest",#插值算法,控制放大时像素之间如何平滑。
                                # "nearest"
                                # 最近邻插值
                                # 每个像素直接放大成方块，边界清晰
                                # "bilinear"
                                # 双线性插值
                                # 颜色平滑过渡
                                # "bicubic"
                                # 三次插值
                                # 更平滑、更柔和
                                # "none"
                                # 不进行插值
                                # 像素原样显示
           cmap="bone",# cmap 是颜色映射表（colormap）
           origin="upper"# 控制坐标 (0,0) 的位置，也就是图像的上下方向。
           )

plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()
