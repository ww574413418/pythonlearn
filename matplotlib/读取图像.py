import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("/Users/grubby/Downloads/gemini-2.5-flash-image-preview (nano-banana)_把iPod变小一些,屏幕显示播放的音乐.png")
plt.imshow(img)
plt.show()