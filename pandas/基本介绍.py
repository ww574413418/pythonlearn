import numpy as np
import pandas as pd

#0    1.0
# 1    NaN
# 2    2.0
# 3    3.0
# dtype: float64
a = pd.Series([1,np.nan,2,3.0])
print(a)

# 日期序列
# DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
#                '2020-01-05', '2020-01-06'],
#               dtype='datetime64[ns]', freq='D')
dates = pd.date_range("20200101",periods=6)
print(dates)

#                    a         b         c         d
# 2020-01-01 -0.105097  0.036308 -1.477368 -0.332488
# 2020-01-02  1.162447  0.575148 -0.132820  0.864374
# 2020-01-03 -0.303595  2.167834 -0.284741 -1.525124
# 2020-01-04  1.784043  0.748264  0.271395  0.581751
# 2020-01-05 -2.625710  0.035726 -1.860803 -0.191141
# 2020-01-06  0.100046  0.164815 -1.314417 -0.657907
# (数据,行名,列名)
df1 = pd.DataFrame(np.random.randn(6,4),index=dates,columns=["a","b","c","d"])
print(df1)

# 不指定行列名默认用0,1,2代替
df2 = pd.DataFrame(np.arange(8).reshape((2,4)))
print(df2)

#DataFrame 要求每一列的长度相同（或者可以广播成相同长度
#    A          B  C     D      E    F
# 0  1 2025-01-01  1     1   test  foo
# 1  1 2025-01-01  1     2  hello  foo
# 2  1 2025-01-01  1  None      1  foo
# 3  1 2025-01-01  1     3    123  foo
df3 = pd.DataFrame(
    {
        "A":1,
        "B":pd.Timestamp("20250101"),
        "C":pd.Series(1,index=list(range(4))),
        "D":np.array(["1",2,None,3]),
        "E":pd.Categorical(["test","hello","1","123"]),
        "F":"foo"
    }
)
print(df3)

# pd里面数据的类型
print(df3.dtypes)
# pd索引
print(df3.index)
# pd的列
print(df3.columns)
# pd的数据
print(df3.values)

#          A                    B    C
# count  4.0                    4  4.0 #数量
# mean   1.0  2025-01-01 00:00:00  1.0 #均值
# min    1.0  2025-01-01 00:00:00  1.0 #最小值
# 25%    1.0  2025-01-01 00:00:00  1.0 #分位数
# 50%    1.0  2025-01-01 00:00:00  1.0 #分位数
# 75%    1.0  2025-01-01 00:00:00  1.0 #分位数
# max    1.0  2025-01-01 00:00:00  1.0 #最大值
# std    0.0                  NaN  0.0 #方差
print(df3.describe())

# 转置
print(df3.T)

# 按列排序 倒叙
print(df3.sort_index(axis=1,ascending=False))
# 按行排序 倒叙
print(df3.sort_index(axis=0,ascending=False))
# 按照值排序
print(df3.sort_values(by="E"))