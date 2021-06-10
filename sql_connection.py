import sqlite3
import time
from datetime import date, datetime
import os.path
from psycopg2 import connect, sql
import psycopg2

def full_read_data():
    con = psycopg2.connect(user="pi",dbname="pi",password="*")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dane")
    dane = cursor.fetchall()
    for x in dane:
        print(x)
    cursor.close()

#class DataBaseConnection():z,x,c,v,b,n

def insert_sensor_data(t,p,h,g,c):
    con = psycopg2.connect(user="pi",dbname="pi",password="*")
    cursor = con.cursor()
    
    query = f"INSERT INTO dane (date,temp,hum,press,gas_res,cpu) VALUES (CURRENT_TIMESTAMP,{t},{p},{h},{g},{c});"

    cursor.execute(query)
    con.commit()
    cursor.close()
    
#insert_sensor_data()
full_read_data()
