import mysql.connector as msql
from mysql.connector import Error
import os
def connect():
    conn= msql.connect(host='localhost', user='root',  password='doro19997')
    try:  
        if conn.is_connected():            
            cursor=conn.cursor()
            print ("[Connection] Connected..")                              
    except Error as e:
        print("Error while connecting to MySQL ", e)
        
    return cursor ,conn
     

def create_db(database):
    """create a database """    
    cursor,conn = connect()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database} ;")
    conn.commit()
    print("Database created..")


def create_table(database):
    """create table"""
    conn,cursor=connect(database)
    sql_file='table.sql'
    f=open(sql_file,'r')
    read_file=f.read()

    sql_commands=read_file.split(';')
    for command in sql_commands:
        try:
            result=cursor.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
        




def main():
    print("[Connection] Establishing a connection to MySql database....")
    connect()
    print("[Create database] ")
    create_db('data')

    
