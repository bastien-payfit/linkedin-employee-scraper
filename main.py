from crawling import mainCrawler
import time


def main(workFiles, batchSize, locations):
    '''
    This function runs the whole scraping rutine to retrieve data from a series of linkedin urls. 
    @params: {dict, int, list}, the dict with the name of the file with linkedin account credentials and the name of the file with input data, the size of each batch of urls to process at a time and the list of xpaths  where to find data
    @returns: {None}
    '''
    startTime = time.time()
    # We reconstitute the xpaths according to the set of locations we're interested in, starting with 'worlwide' and the total number of employees
    nbLocations = len(locations)
    xpaths = ['//*[@id="main"]/div[2]/div/div[1]/div[1]/span/text()']
    for i in range(nbLocations):
        xpaths.append(f'//span[@class="org-people-bar-graph-element__category" and contains(text(), "{locations[i]}")]/preceding-sibling::strong/text()')
    locations = ["totalHeadcount"] + locations
    mainCrawler(workFiles, xpaths, batchSize)
    endTime = time.time()
    print(f'Runtime: {endTime - startTime}') 

## PARAMETERS BELOW ##

workFiles = {
    "source": "test.csv", # 👈 PUT THE NAME OF YOUR INPUT CSV FILE HERE 
    "credentials": "linkedinBastien.csv" # 👈 PUT THE NAME OF THE CSV FILE WITH YOUR CREDENTIALS HERE (YOU COULD BE USING MULTIPLE LINKEDIN ACCOUNTS)
}

main(workFiles, 1, ["Allemagne"])

