import numpy as np

a = np.arange(4)

b = a
c = a
d = a.copy()
print()

a[0] = 11

print(a)
print(b)
print(c)
# 不会改变
print(d)


