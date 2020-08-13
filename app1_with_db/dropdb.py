import mysql.connector as mysql
try:
    con=mysql.connect(
        user='root',
        password='12369478521',
        host='localhost',
        database='Dictionary'
    )
    cursor=con.cursor()
    cursor.execute('DROP DATABASE IF EXISTS Dictionary')
except Exception as ex:
    print(ex.__str__())
print('your database droped')
