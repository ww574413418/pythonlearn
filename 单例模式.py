# 重写__new__()方法
class Single:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if(cls.__instance == None):
            cls.__instance = super().__new__(cls)
        return cls.__instance


a1 = Single()
a2 = Single()

print(a1 == a2)

from pytest import test as test01
from pytest import test as test02

print(test01 == test02)