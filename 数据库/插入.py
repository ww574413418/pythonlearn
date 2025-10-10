from datetime import datetime

from pymysql import Connection

cnn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="hmall"
)
cursor = cnn.cursor()
sql = "insert into user(username,password,phone,create_time,update_time) values(%s,%s,%s,%s,%s)"
values = ("jerry","1234","13325244340",datetime.now(),datetime.now())

cursor.execute(sql,values)
cnn.commit()

cursor.close()