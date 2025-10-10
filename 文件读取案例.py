'''
读取文件
将文件写出到bill.txt.bak文件作为备份
同时, 将文件内标记为测试的数据行丢弃
'''

file1 = open("/Users/grubby/Downloads/test.txt","r",encoding="UTF-8")
file2 = open("/Users/grubby/Downloads/bill.txt.bak","a",encoding="UTF-8")
for line in file1:
    if(line.count("测试") > 0):
        continue
    file2.write(line)
file1.close()
file2.flush()
file2.close()