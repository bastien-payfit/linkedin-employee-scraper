import csv
import pickle as pk
import os

def credsRetriever(filename:str) -> str:
    with open("./credentials/" + filename, 'r') as f:
        creds = [row for row in csv.reader(f)]
    return creds[0]

def openCSV(sourceFileName:str, targetFileName: str) -> list:
    with open("./data/" + sourceFileName, "r") as f2:
        dataSource = [row for row in csv.reader(f2)]
        # print(f'Data source: {dataSource}')
    if targetFileName in os.listdir("./data"):
        with open("./data/" + targetFileName, "r") as f1:
            targetData = [row for row in csv.reader(f1)]
            # print(f'Target data: {targetData}')
    else:
        with open("./data/" + targetFileName, "w") as empty_csv:
            targetData = []
    return dataSource, targetData