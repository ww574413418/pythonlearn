'''
file_util.py (文件处理相关工具, 内含：)
• 函数：Print_file_info (file_name) , 接收传入文件的路径, 打印文件的全部内
容, 如文件不存在则捕获异常, 输出提示信息, 通过finally关闭文件对象
• 函数：append_to_file (file_name, data) , 接收文件路径以及传入数据, 将数据
追加写入到文件中
'''
def print_file_info(fie_name):
    file = None
    try:
        file = open(fie_name,"r",encoding="UTF-8")
        lines = file.readlines()
        print(lines)
    except FileNotFoundError:
        print("there are not exit the file")
    finally:
        if file:
            file.close()


def append_to_file (file_name, data):
    file = None
    try:
        file = open(file_name,"a",encoding="UTF-8")
        file.write(data)
    except:
        print("the file is not exist")
    finally:
        if file:
            file.close()

if __name__ == '__main__':
    file_name = "/Users/grubby/Downloads/myutils.txt"
    print_file_info(file_name)
    append_to_file(file_name,"grubby")