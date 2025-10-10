import numpy as np
import matplotlib.pyplot as plt

def step_fun(x):
    y = x > 0
    return y.astype(int)


x = np.arange(-5,5,1)
y = step_fun(x)
plt.step(x, y, where="mid")
plt.show()