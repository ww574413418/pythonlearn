import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 线性图
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()

# dataframe
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
print(data.head(5))
data = data.cumsum()
data.plot()
plt.show()

# 散列表
ax = data.plot.scatter(x="A",y="B",label="Class 1")
data.plot.scatter(x="A",y="C",color="red",label="Class 2",ax = ax)
plt.show()