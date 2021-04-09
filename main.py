from crawling import mainCrawler
import time


def main(workFiles, batchSize, xpaths = ['//a[@data-control-name="visit_company_website"]/@href']):
    '''
    This function runs the whole scraping rutine to retrieve data from a series of linkedin urls. 
    @params: {dict, int, list}, the dict with the name of the file with linkedin account credentials and the name of the file with input data, the size of each batch of urls to process at a time and the list of xpaths  where to find data
    @returns: {None}
    '''
    startTime = time.time()
    mainCrawler(workFiles, xpaths, batchSize)
    endTime = time.time()
    print(f'Runtime: {endTime - startTime}') 

workFiles = {
    "source": "gemeinsam1.csv",
    "credentials": "linkedinGauvain.csv"
}

# xpath = '//a[@data-control-name="all_employees_search_link"]/text()'
# xpath = '//span[@class="org-people-bar-graph-element__category" and contains(text(), "France")]/preceding-sibling::strong/text()'

batchSize = 19
totalEmployees = '//*[@id="main"]/div[2]/div/div[1]/div[1]/span/text()'
germanEmployees = '//span[@class="org-people-bar-graph-element__category" and contains(text(), "Allemagne")]/preceding-sibling::strong/text()'

main(workFiles, batchSize, xpaths = [germanEmployees, totalEmployees])

