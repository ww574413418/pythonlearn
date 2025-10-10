from 数据分析案例.file_operation_def import textFileReader
from 数据分析案例.file_operation_def import JsonFileReader
from 数据分析案例.Record import Record
from pymysql import Connection

textFile = textFileReader("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/数据分析案例/2011年1月销售数据.txt")
jsonFile = JsonFileReader("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/数据分析案例/2011年2月销售数据JSON.txt")

text_data_list:list[Record] = textFile.fileReader()
json_data_list:list[Record] = jsonFile.fileReader()

all_data_list = text_data_list + json_data_list

# 建立数据库链接
cnn = Connection(
    user="root",
    password="root",
    host="localhost",
    port=3306,
    database="python_learn"
)

cursor = cnn.cursor()

sql = "insert into orders(order_date,order_id,money,province) values(%s,%s,%s,%s)"
'''
values = []
for data in all_data_list:
    values.append((data.date, data.order_id, data.money, data.province))
'''
values = [(data.date, data.order_id, data.money, data.province) for data in all_data_list]

cursor.executemany(sql,values)

cnn.commit()
cnn.close()