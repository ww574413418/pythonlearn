# 定义一个元组, 内容是：
#  ('周杰轮, 11, ［football, 'music')
# 记录的是一个学生的信息 (姓名、“
# 请通过元组的功能 (方法) , 对其进行
# 1. 查询其年龄所在的下标位置
# 2. 查询学生的姓名
# 3.  删除学生爱好中的football
# 4. 增加爱好：coding到爱好list内

my_tuple = ("jay",11,["football","music"])

index = my_tuple.index(11)
name = my_tuple[1]
my_tuple[2].pop(0)
my_tuple[2].insert(0,"coding")
print(my_tuple)