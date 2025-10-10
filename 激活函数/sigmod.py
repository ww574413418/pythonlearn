import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))
def identity_function(x):
    return x

if __name__ == '__main__':
    x = np.arange(-5,5,1)
    y = sigmoid(x)
    plt.ylim(-0.1, 1.1)
    plt.plot(x,y)
    plt.show()