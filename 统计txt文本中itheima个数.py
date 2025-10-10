'''
/Users/grubby/Downloads/test.txt
统计test文本中itheima的个数
'''

file = open("/Users/grubby/Downloads/test.txt","r",encoding="UTF-8")
count = 0
for line in file:
    # 使用strip来去除首尾空白，再按照空白字符分割
    str_list = line.strip().split(" ")
    count +=str_list.count("itheima")

file.close()
print(count)