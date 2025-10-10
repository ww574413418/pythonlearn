class person(object):
    name = "Tom"
    @staticmethod
    def say(word):
        print(word)

    @classmethod
    def sleep(cls):
        print(cls.name)

person.say("hello")
person.sleep()

class Person:
    default_name = "Anonymous"

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_default(cls):
        return cls(cls.default_name)  # 使用 cls 创建实例

p = Person.create_default()
print(p.name)  # "Anonymous"（调用了类方法构造实例）