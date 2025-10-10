# 文件操作接口
import json

from 数据分析案例.Record import Record

class file_operation:

    def fileReader(self)->list[Record]:
        '''
        读取文件,并封装到data中
        :return: list[data]
        '''
        pass


class textFileReader(file_operation):
    '''
    deal with csv type file
    '''
    file_path = None

    def __init__(self,file_path):
        self.file_path = file_path

    def fileReader(self) ->list[Record]:
        '''
        load csv data text and transfer it into python object
        :return: list[Record]
        '''
        try:
            file = open(self.file_path,"r",encoding="UTF-8")
            data_list:list[Record] = list()
            for line in file.readlines():
                datas = line.strip().split(",")
                my_data = Record(datas[0],datas[1],int(datas[2]),datas[3])
                data_list.append(my_data)
            return data_list
        except FileNotFoundError:
            print("the file is not exist")
        finally:
            file.close()


class JsonFileReader(file_operation):
    '''
        solve json type data
    '''
    file_path = None

    def __init__(self,file_path):
        self.file_path = file_path

    def fileReader(self) ->list[Record]:
        '''
        load json text and transfer it into python object
        :return: list[Record]
        '''
        try:
            file = open(self.file_path,"r",encoding="UTF-8")
            lines = file.readlines()
            data_list:list[Record] = list()
            for line in lines:
                data:dict = json.loads(line.strip())
                record = Record(data["date"],data["order_id"],data["money"],data["province"])
                data_list.append(record)

            return data_list
        except FileNotFoundError:
            print("the file is not exist")
        finally:
            file.close()


if __name__ == '__main__':
    reader = textFileReader("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/数据分析案例/2011年1月销售数据.txt")
    data_list = reader.fileReader()
    print(data_list)

    reader = JsonFileReader("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/数据分析案例/2011年2月销售数据JSON.txt")
    data_list = reader.fileReader()
    print(data_list)
