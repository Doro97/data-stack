import pandas as pd
import csv
# import requests


path='E:\Data engineering projects\data-stack\data-stack\yellow_tripdata_2021-01 (1).csv'
def view_file():
    """function that takes in the file-path and returns the first row of the csv file"""
    with open (path, mode='r',encoding="windows-1252") as csv_file:
        reader=csv.DictReader(csv_file)
        # get the first row
        row=next(reader)
        print("[Extract] Printing the first row: ", row)        


def main():
    print("[Extract] Start...")   
    view_file()
    print("[Extract] End...")

  