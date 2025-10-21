import numpy as np
import pandas as pd

dates = pd.date_range("20250101",periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])
df.iloc[2,2] = np.nan
df.iloc[3,1] = np.nan
#              A     B     C   D
# 2025-01-01   0   1.0   2.0   3
# 2025-01-02   4   5.0   6.0   7
# 2025-01-03   8   9.0   NaN  11
# 2025-01-04  12   NaN  14.0  15
# 2025-01-05  16  17.0  18.0  19
# 2025-01-06  20  21.0  22.0  23
print(df)

# 按行丢掉null数据,how=any 有一个0删除一行,all 全部为0删除一行
#              A     B     C   D
# 2025-01-01   0   1.0   2.0   3
# 2025-01-02   4   5.0   6.0   7
# 2025-01-05  16  17.0  18.0  19
# 2025-01-06  20  21.0  22.0  23
print(df.dropna(axis=0,how="any"))

# 按列丢
#              A   D
# 2025-01-01   0   3
# 2025-01-02   4   7
# 2025-01-03   8  11
# 2025-01-04  12  15
# 2025-01-05  16  19
# 2025-01-06  20  23
print(df.dropna(axis=1,how="any"))

# 将null变成0
#              A     B     C   D
# 2025-01-01   0   1.0   2.0   3
# 2025-01-02   4   5.0   6.0   7
# 2025-01-03   8   9.0   0.0  11
# 2025-01-04  12   0.0  14.0  15
# 2025-01-05  16  17.0  18.0  19
# 2025-01-06  20  21.0  22.0  23
print(df.fillna(value=0))

# 检查是否存在null数据
#                 A      B      C      D
# 2025-01-01  False  False  False  False
# 2025-01-02  False  False  False  False
# 2025-01-03  False  False   True  False
# 2025-01-04  False   True  False  False
# 2025-01-05  False  False  False  False
# 2025-01-06  False  False  False  False
print(df.isnull())

# 表很大的情况查看是否有null值
# True
print(np.any(df.isnull()) == True)


