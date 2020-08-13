import mysql.connector as mysql
import json
try:
    con=mysql.connect(
        user='root',
        password='12369478521',
        host='localhost',
    )
    cursor=con.cursor()
    cursor.execute('create database if not exists Dictionary')
    cursor.execute('use Dictionary')
    cursor.execute('create table if not exists words(id int not null auto_increment primary key ,word varchar(200),definition varchar(6000))')
except Exception as ex:
    print(ex.__str__())

data=json.load(open('/home/mahmoud/PycharmProjects/python_meaga_course/app1/data.json'))


try:
    for key,values in data.items():
        for value in values:
            cursor.execute('insert into words(word,definition) values (%s,%s)',(key,value))
    con.commit()

except Exception as ex:
    print(ex.__str__(),' this for insertion error ')

print('your database is now ready you can run app1_with_db.py now')


