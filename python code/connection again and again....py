import pandas as pd
import mysql.connector as sql
my=sql.connect(host="localhost",user="root",
               passwd="mynameismanu",
               database="privatecompany")
if my.is_connected():
  print("oh bhai")
