# 有一个列表, 内容是：［21, 25, 21, 23, 22,  20］, 记录的是一批学生的年龄
# 请通过列表的功能 (方法) , 对其进行
# 1.定义这个列表, 并用变量接收它
# 2. 追加一个数字31, 到列表的尾部
# 3.追加一个新列表［29,33, 30］, 到列表的尾部
# 4. 取出第一个元素 (应是：21)
# 5. 取出最后一个元素 (应是：30)
# 6. 查找元素31, 在列表中的下标位置

list = [21, 25, 21, 23, 22,  20]

list.append(31)
print(list)
extent_list = [29,33, 30]
list.extend(extent_list)
print(list)

list[0]
print(list[0])

print(list[len(list)-1])

index = list.index(31)
print(index)

# 定义一个列表, 内容是：［1, 2,3, 4, 5, 6,7,8, 9, 10]
# 遍历列表, 取出列表内的偶数, 并存入一个新的列表对象中
# 使用while循环和for循环各操作一次
mylist = [1, 2,3, 4, 5, 6,7,8, 9, 10]
event_list = []
odd_list = []
for i in mylist:
    if i % 2 == 0:
        event_list.append(i)
    else:
        odd_list.append(i)

print(event_list)
print(odd_list)

index = 0
event_list2 = []
odd_list2 = []
while index < len(mylist):
    if mylist[index] % 2 == 0:
        event_list2.append( mylist[index])
    else:
        odd_list2.append( mylist[index])
    index += 1

print(event_list2)
print(odd_list2)