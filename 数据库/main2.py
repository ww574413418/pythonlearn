import json
from datetime import datetime

from 数据分析案例.Record import Record
from pymysql import Connection


cnn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="python_learn",
    autocommit=True
)

cursor = cnn.cursor()

sql = "select order_date,order_id,money,province from orders"

cursor.execute(sql)
result = cursor.fetchall()
Record_list = []
for data in result:
    record= Record()
    record.date = data[0].strftime("%Y-%m-%d")
    record.order_id = data[1]
    record.money = data[2],
    record.province = data[3]

    Record_list.append(record)


cnn.close()


# 替换 json.dumps(Record_list)
json_str = json.dumps([r.to_dict() for r in Record_list], ensure_ascii=False, indent=4)

file = open("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/数据库/order.txt","a",encoding="UTF-8")
file.write(json_str + "/n")
file.close()
