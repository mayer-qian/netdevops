import mysql.connector

conn = mysql.connector.connect(
    host='10.167.0.x',
    user='xxx', password='xxx',
    database='Network',
    charset='utf8'

)
cursor = conn.cursor()
cursor.execute("select * from Host where Code_site='sha'")
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
