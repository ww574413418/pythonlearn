'''
•定义一个全局变量：money, 用来记录银行卡余额 (默认5000000)
•定义一个全局变量：name, 用来记录客户姓名 (启动程序时输入)
•定义如下的函数：
• 查询余额函数
• 存款函数
• 取款函数
• 主菜单函数
• 要求：
程序启动后要求输入客户姓名
查询余额、存款、取款后都会返回主菜单
存款、取款后, 都应显示一下当前余额
客户选择退出或输入错误, 程序会退出, 否则一直运行
'''

import os

money = 5000000
name = None

flag = True

def get_balance():
    global money
    print(money)

def withdrawal(num):
    # 声明money是全局变量
    global money
    money = money - num
    print(f"取款的金额为{num},余额为{money}")

def deposit(num):
    global money
    money = money + num
    print(f"存款的金额为{num},余额为{money}")

def main():
    print("*********主菜单** *******")
    print("***1,查询余额***********")
    print("***2,取款***************")
    print("***3,存款***************")
    print("***4,退出***************")
    return input("请输入功能:")

def clear_console():
   os.system('clear')


while flag:
    name = input("请输入姓名")
    keyboard_input = int(main())
    if keyboard_input == 1:
        get_balance()
        clear_console()
        continue
    elif keyboard_input == 2:
        num = int(input("请输入取款金额"))
        withdrawal(num)
        clear_console()
        continue
    elif keyboard_input == 3:
        num = int(input("请输入存款金额"))
        deposit(num)
        clear_console()
        continue
    else:
        flag = False;
