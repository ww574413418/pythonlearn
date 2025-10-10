

# 现在我们让这个person可以唱歌

def outter(fun):
    # 加强函数
    def inner():
        fun()
        print("我可以唱歌")
    return inner


@outter
def person():
    print("我可以跳舞")

person()


def outter2(fun ):
    def inner(name):
        fun
        print(f"{name}是inner里面的name")

    return inner

@outter2
def test(name):
    print("这是test")

test("hello")


def outter3(fun):
    def inner(*args,**kwargs):
        fun
        print(f"*args是:{args}")
    return inner

@outter3
def test2(*args,**kwargs):
    print("这是test2")

test2([1,"hello",False],{1:"hello",2:"world"})


# 装饰器1
def deco1(fun):
    def inner():
        return "AAA" + fun() + "BBB"
    return inner

# 装饰器2
def deco2(fun):
    def inner():
        return "----" + fun() + "----"
    return inner

@deco1
@deco2
def test3():
    return "aaa"


print(test3())#AAA----aaa----BBB