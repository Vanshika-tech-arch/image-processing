import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="" ,
  database="ABOUTINFO"
)
mycursor =mydb.cursor()

#mycursor.execute("CREATE DATABASE ABOUTINFO")
#mycursor.execute("CREATE TABLE STUDENT (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
for x in range(5):
    a =input("plz enter name")
    b =input("enter address")
    print("hello {0} ,you live in {1}".format(a,b))
mycursor.execute(a, b)
sql = "INSERT INTO STUDENT (name, address) VALUES (%s, %s)"
val = (a,b)
mycursor.executemany(sql, val)

mydb.commit()
mydb.commit()