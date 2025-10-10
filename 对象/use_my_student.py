from Student import *

i=0
name = None
age = None
address = None

for i in range(10):
    name = input("请输入姓名:")
    age = int(input("请输入年龄:"))
    addres = input("请输入地址:")
    stu = Student(name,age,addres)
    print(stu)

