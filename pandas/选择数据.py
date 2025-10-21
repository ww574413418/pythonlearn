import numpy as np
import pandas as pd

dates = pd.date_range("20200101",periods=6)

df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])
#              A   B   C   D
# 2020-01-01   0   1   2   3
# 2020-01-02   4   5   6   7
# 2020-01-03   8   9  10  11
# 2020-01-04  12  13  14  15
# 2020-01-05  16  17  18  19
# 2020-01-06  20  21  22  23
print(df)
# 取A列
print(df["A"])
print(df.A)
# 取行
print(df[0:3]) # 0~3行
print(df["2020-01-01":"2020-01-03"])

# select by label:loc
# A    16
# B    17
# C    18
# D    19
# Name: 2020-01-05 00:00:00, dtype: int64
print(df.loc["2020-01-05"])
#(行数据,列数据)
print(df.loc[:,["A","B"]])
print(df.loc["2020-01-06",["A","B"]])

# select by positioin:iloc
# 第三行第一位
print(df.iloc[3,1])
# 3~5行,1~2列
print(df.iloc[3:5,1:2])

# boolean select
# 找到A大于8的
print(df[df.A > 8])