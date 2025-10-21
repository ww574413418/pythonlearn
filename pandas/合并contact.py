import numpy as np
import pandas as pd

#合并多个dataframe相同的column
df1 = pd.DataFrame(np.ones((3,4)) * 0,columns=["a","b","c","d"])
df2 = pd.DataFrame(np.ones((3,4)) * 1,columns=["a","b","c","d"])
df3 = pd.DataFrame(np.ones((3,4)) * 2,columns=["a","b","c","d"])

# ignore_index 忽略到原来的index
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)

# 行列不完全一样的合并
df4 = pd.DataFrame(np.ones((3,4))*0,columns=["a","b","c","d"],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*1,columns=["b","c","d","e"],index=[2,3,4])

#并集
res = pd.concat([df4,df5],join="outer",ignore_index=True)
#      a    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  0.0  0.0  0.0  0.0  NaN
# 2  NaN  1.0  1.0  1.0  1.0
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0
print(res)

# 交集
res = pd.concat([df4,df5],join="inner",ignore_index=True)
#      b    c    d
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  0.0  0.0  0.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0
print(res)


