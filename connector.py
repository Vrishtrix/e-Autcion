import mysql.connector as mc

mydb = mc.connect(
      host='localhost',
      user='root',
      password='hello123',
      database='auction'
)

mycursor = mydb.cursor()