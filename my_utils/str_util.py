'''
创建一个自定义包, 名称为：my_utils (我的工具)
在包内提供2个模块
• str_util.py (字符串相关工具, 内含：)
• 函数：str_reverse (s) , 接受传入字符串, 将字符串反转返回
• 函数：substr  (s,x, y) , 按照下标x和y, 对字符串进行切片

'''

def str_reverse(s):
    ReStr = s[::-1]
    return ReStr

def substr(s,x,y):
    subStr = s[x:y:1]
    return subStr

if __name__ == '__main__':
    str = "hello world"
    str_reverse(str)
    substr(str)