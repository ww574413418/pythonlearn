class Person:
    __age = 30  # 这里使用单下划线表示保护属性

    def __init__(self, age):  # 构造函数应该是 __init__，而不是 __int__
        self.__age = age  # 通过构造函数给 _age 赋值


person = Person(25)

# 通过名称重整访问私有属性 __age
print(person._Person__age)