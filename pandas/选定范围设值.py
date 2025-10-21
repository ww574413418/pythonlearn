import numpy as np
import pandas as pd

dates = pd.date_range("20250101",periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=["A","B","C","D"])
print(df)

# 第二行第二列改成111
df.iloc[2,2] = 111
print(df)

# 将2025-01-02 行的第D列改成999
df.loc["2025-01-02 ","D"] = 999
print(df)

# 将A列中大于4的整行都变成0
df[df.A > 4] = 0
#             A  B  C    D
# 2025-01-01  0  1  2    3
# 2025-01-02  4  5  6  999
# 2025-01-03  0  0  0    0
# 2025-01-04  0  0  0    0
# 2025-01-05  0  0  0    0
# 2025-01-06  0  0  0    0
print(df)

df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=["A","B","C","D"])

# 将A列中大于4的变成0
df.loc[df.A > 4,"A"] = 0
#             A   B   C   D
# 2025-01-01  0   1   2   3
# 2025-01-02  4   5   6   7
# 2025-01-03  0   9  10  11
# 2025-01-04  0  13  14  15
# 2025-01-05  0  17  18  19
# 2025-01-06  0  21  22  23
print(df)

# 添加新的一列null
df["F"] = np.nan
print(df)

# 添加一列非空
df["E"] = pd.Series([1,2,3,4,5,6],index=dates)
print(df)

# 添加一行
df.loc["2025-01-07"] = pd.Series([1,2,3,4,5,6],index=["A","B","C","D","E","F"])
print(df)
