import numpy as np
import pandas as pd

left = pd.DataFrame({
    "key":["k0","k1","k2","k3"],
    "a":["a0","a1","a2","a3"],
    "b":["b0","b1","b2","b3"]
})

right = pd.DataFrame({
    "key":["k0","k1","k2","k3"],
    "c":["c0","c1","c2","c3"],
    "d":["d0","d1","d2","d3"]
})

print(left)
print(right)

res = pd.merge(left,right,on="key")
#   key   a   b   c   d
# 0  k0  a0  b0  c0  d0
# 1  k1  a1  b1  c1  d1
# 2  k2  a2  b2  c2  d2
# 3  k3  a3  b3  c3  d3
print(res)

left = pd.DataFrame({
    "key1":["k0","k0","k1","k2"],
    "key2":["k0","k1","k0","k1"],
    "a":["a0","a1","a2","a3"],
    "b":["b0","b1","b2","b3"]
})

right = pd.DataFrame({
    "key1":["k0","k1","k1","k2"],
    "key2": ["k0", "k0", "k0", "k0"],
    "c":["c0","c1","c2","c3"],
    "d":["d0","d1","d2","d3"]
})

res = pd.merge(left,right,on=["key1","key2"],how="inner")
#   key1 key2   a   b   c   d
# 0   k0   k0  a0  b0  c0  d0
# 1   k1   k0  a2  b2  c1  d1
# 2   k1   k0  a2  b2  c2  d2
print(res)

df1 = pd.DataFrame({
    "col1":[0,1],
    "col_left":["a","b"],
})

df2 = pd.DataFrame({
    "col1":[0,1,2],
    "col_right":[2,2,2],
})
print(df1)
print(df2)

#indicator 现实merge的方式
res = pd.merge(df1,df2,on="col1",how="outer",indicator=True,)
print(res)

# 通过index合并
left = pd.DataFrame({
    "A":["A0","A1","A2"],
    "B":["B0","B1","B2"],
},index=["K0","K1","K2"])

right = pd.DataFrame({
    "C":["C0","C1","C2"],
    "D":["D0","D1","D2"],
},index=["K0","K2","K3"])

res = pd.merge(left,right,left_index=True,right_index=True,how="outer")
print(res)

boys = pd.DataFrame({
    "k": ["K0","K1","K2"],
    "age":[1,2,3]
})

girls = pd.DataFrame({
    "k": ["K0","K0","K3"],
    "age":[4,5,6]
})

res = pd.merge(boys,girls,on="k",suffixes=["_boy","_girl"],how="inner")
print(res)


