from crawling import mainCrawler
import time

def main(workFiles, batchSize, locations):
    '''
    This function runs the whole scraping rutine to retrieve data from a series of linkedin urls. 
    @params: {dict, int, list}, the dict with the name of the file with linkedin account credentials, the index of the column with linkedin urls and the name of the file with input data, the size of each batch of urls to process at a time and the list of xpaths  where to find data
    @returns: {None}
    '''
    startTime = time.time()
    mainCrawler(workFiles, batchSize, locations)
    endTime = time.time()
    print(f'Runtime: {endTime - startTime}') 



######################################################## PARAMETERS BELOW #########################################################

workFiles = {
    "source": "test.csv", # 👈 PUT THE NAME OF YOUR INPUT CSV FILE HERE 
    "linkedinUrlColumnIndex": 1, # 👈 PUT THE INDEX OF THE COLUMN WITH THE LINKEDIN URLS IN YOUR INPUT CSV (INDEXES START AT 0)
    "credentials": "linkedinBastien.csv" # 👈 PUT THE NAME OF THE CSV FILE WITH YOUR CREDENTIALS HERE (YOU COULD BE USING MULTIPLE LINKEDIN ACCOUNTS)
}
batchSize = 10
locations = ["Allemagne"] # 👈 PUT THE LOCATIONS WHERE YOU WANT TO FIND THE NUMBER OF EMPLOYEES. BEWARE! IF YOUR LINKEDIN ACCOUNT IS IN FRENCH YOU PUT 'ALLEMAGNE' IF IT'S IN ENGLISH YOU PUT 'GERMANY'






######################################################## CALL TO THE MAIN FUNCTION ########################################################
main(workFiles, batchSize, locations)

