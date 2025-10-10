class Student:
    name:None
    age:None
    address:None

    # 构造方法
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        print("执行了构造方法")

    def __str__(self):
        return f"Student对象,name={self.name},age={self.age},address={self.address}"

    def __lt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age
    def sayHello(self,msg):
        print(f"大家好,是我{self.name},{msg}")


if __name__ == '__main__':
    Stu = Student()
    Stu.name = "grubby"
    Stu.age = 12
    Stu.sayHello("哎哟不错哦")