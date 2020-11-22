import mysql.connector as mc

mydb = mc.connect(
      host='localhost',
      user='root',
      password='Hello@123',
      database='auction',
      autocommit=True
)

mycursor = mydb.cursor()