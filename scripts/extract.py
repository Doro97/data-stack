import pandas as pd
import csv
import requests

path='https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv'
def view_file():
    """function that takes in the file-path and returns the first 5 rows of the csv file"""
    file=pd.read_csv(path)
    file=file.head()
    return file

def main():
    print("[Extract] Start...")
    print("[Extract] View the first 5 lines in the file...")
    view_file()
    print("[Extract] End...")
