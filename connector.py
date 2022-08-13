import os
import mysql.connector as mc

mydb = mc.connect(
      host='localhost',
      user='root',
      password=os.environ["PASSWORD"],
      database='auction',
      autocommit=True
)

mycursor = mydb.cursor()
