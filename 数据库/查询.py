from pymysql import Connection

cnn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="hmall"
)

print(cnn.get_server_info())

# 只从sql查询
cursor = cnn.cursor()
cursor.execute("select * from user")
print("Current Database:", cursor.fetchone())
cnn.close()
