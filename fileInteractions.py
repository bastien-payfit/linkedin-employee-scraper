import csv
import pickle as pk
import os

def credsRetriever(filename:str) -> str:
    '''
    This function returns the email and password of a linkedin account stored in a csv file in the credentials folder.
    @params: {str} the name of the credentials file
    @returns: {list} a list with first the email and then the password to the linkedin account
    '''
    with open("./credentials/" + filename, 'r') as f:
        creds = [row for row in csv.reader(f)]
    return creds[0]

def openCSV(sourceFileName:str, targetFileName: str) -> list:
    '''
    The function opens both csv files: the one with data to scrape when the other with scraping results and returns the csv data in form of list of lists
    @params: {str, str} the names of both files (input and result) to find in the data folder
    @returns: {list, list} the lists of data encompassed in both files (the first being the datasource and the other being the result data)
    '''
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