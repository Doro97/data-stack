import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
from extract import data_frame

path='E:\Data engineering projects\data-stack\data-stack\yellow_tripdata_2021-01 (1).csv'
def connect():
    conn = msql.connect(host='localhost', user='root',  password='doro19997')
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            print("[Connection] Connected..")
    except Error as e:
        print("Error while connecting to MySQL ", e)

    return cursor, conn


def create_db_table(database, table):
    """create a database """
    cursor, conn = connect()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database} ;")
    conn.commit()
    print("Database created..")
    cursor.execute(f"CREATE TABLE {database}.{table}(VendorID INT NOT NULL,tpep_pickup_datetime DATE NOT NULL, tpep_dropoff_datetime DATE NOT NULL, passenger_count INT NOT NULL,trip_distance FLOAT NOT NULL, RatecodeID INT NOT NULL, store_and_fwd_flag VARCHAR (20) NOT NULL,PULocationID INT NOT NULL,DOLocationID INT NOT NULL,payment_type INT NOT NULL,fare_amount INT NOT NULL,extra INT NOT NULL, mta_tax FLOAT NOT NULL, tip_amount INT NOT NULL,tolls_amount INT  NOT NULL,improvement_surcharge FLOAT NOT NULL,total_amount FLOAT NOT NULL,congestion_surcharge FLOAT NOT NULL);")
    conn.commit()
    print("Table created..")   


def insert_data(database,table):
    """insert records from a data frame into the database"""
    conn,cursor=connect()
    df=pd.read_csv(path)

    for _, row in df.iterrows():
        query=f"""INSERT INTO {database}.{table}(VendorID,tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count,trip_distance , RatecodeID, store_and_fwd_flag,PULocationID ,DOLocationID,payment_type,fare_amount,extra, mta_tax, tip_amount,tolls_amount,improvement_surcharge,total_amount,congestion_surcharge)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        data=(row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8],
        row[9], row[10], row[11],row[12], row[13], row[14])
        cursor.execute(query,data)
        conn.commit()
        print("Data inserted successfully")

def main():
    print("[Connection] Establishing a connection to MySql database....")
    connect()
    # print("[Create database and table..] ")
    # create_db_table('tripdata', 'data')
    # print("[Create table]")
    # create_table('tripdata')
    print("[Inserting data into the table..]")
    insert_data('tripdata','data')
