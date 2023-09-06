import mysql.connector
from mysql.connector import Error



def consultar(consulta):
    mycursor.execute(consulta)
    return(mycursor.fetchall())

mydb = mysql.connector.connect (
  host="us-cdbr-east-06.cleardb.net",
  user="b5a61052eef78e",
  password="a936c0dd",
  database="heroku_416c78d4e3ba909"
)

mycursor = mydb.cursor()