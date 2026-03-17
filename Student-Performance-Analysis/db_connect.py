import mysql.connector
import pandas as pd

def get_connection():
 conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1167",
    database="student_analysis"
 )
 return conn