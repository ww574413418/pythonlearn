import numpy as np

def  mean_squared_error(predicts,targets):
    return 0.5 * np.sum((predicts - targets)**2)