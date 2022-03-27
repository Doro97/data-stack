import pandas as pd
import csv
import requests

def view_file(path: str):
    """function that takes in the file-path and returns the first 5 rows of the csv file"""
    file=pd.read_csv(path)
    file=file.head()
    return file

