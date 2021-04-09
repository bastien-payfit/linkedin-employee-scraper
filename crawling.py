from selenium import webdriver
from parsel import Selector
from utils import *
import csv
from fileInteractions import *

# Open driver
def openDriver(driverPath = '/Users/bastienvelitchkine/Documents/Code/chromedriver'):
    '''
    This function opens a driver with selenium and chrome driver. You can see selenium as a puppeteer and chromedriver as the puppet. What happens is the puppeteer tied links between its hands and the puppet.
    @params: {str} the path to chromedriver on your machine
    @returns: {driver}, a driver instance according to selenium's description of a driver
    '''
    driver = webdriver.Chrome(driverPath)
    return driver

# Connection to linkedin
def linkedinConnect(driver, email, pwd):
    '''
    Given a driver, the email id and password of a linkedin account and a site to visit, this function automatically connects the driver instance to linkedin.
    @params: {driver, str, str} a driver according to selenium's definition, the email of the linkedin account and the associated password.
    @returns: {None}
    '''
    driver.get("https://www.linkedin.com")
    try:
        username = driver.find_element_by_id('session_key')
        username.send_keys(email)
        sleepShortTime()
        password = driver.find_element_by_id('session_password')
        password.send_keys(pwd)
        sleepShortTime()
        log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
        log_in_button.click()
        sleepShortTime()
    except: # If an exception was raised, it's most likely because the page architecture was not the one expected and form inputs had different ids
        log_in_button = driver.find_element_by_class_name('form-toggle')
        log_in_button.click()
        sleepShortTime()
        username = driver.find_element_by_class_name('login-email')
        username.send_keys(email)
        sleepShortTime()
        password = driver.find_element_by_class_name('login-password')
        password.send_keys(pwd)
        sleepShortTime()
        log_in_button = driver.find_element_by_class_name('login submit-button')
        log_in_button.click()

def domainCrawler(driver, url, xpaths):
    '''
    This is a single url crawler. Once the driver is connected to linkedin, this function tries to visit a specific linkedin url and retrieve the data found at the specified xpaths (in our case linkedin employees in a specific location).
    @params: {driver, str, list} the driver according to selenium's definition, the url to visit, the list of xpaths where we want to collect data.
    @returns: {list} the list of data pieces extracted at the specified xpaths. If two xpaths were given, we can expect two elements in this list.
    '''
    print(f'Last crawled url: {url}')
    res = []
    try:
        driver.get(url)
        sleepShortTime()
        sel = Selector(text = driver.page_source)
        for xpath in xpaths:
            try: 
                extract = sel.xpath(xpath).extract_first()
                temp = "".join([char for char in extract if char not in '\n" '])
            except: # LinkedIn blocked or the xpath did not exist
                temp = None
            res.append(temp)
    except: # The driver could not visit the url
        res = len(xpaths)*["error"]
    print(f"result {res}")
    return res

def domainsCrawler(dataToScrape, xpaths, targetWriter, credsPath):
    '''
    This function scrapes multiple linkedin urls to find the number of employees in specific locations and writes the results in a csv file.
    @params {list, list, csv writer, str} the input csv lines containing the url to scrape, the xpaths where to find the data, the csv writer where we write our results, the path to the linkedin credentials.
    @returns {None}
    '''
    driver = openDriver()
    credentials = credsRetriever(credsPath)
    linkedinConnect(driver, credentials[0], credentials[1])
    res = []
    bugDetector = 0
    for i, elem in enumerate(dataToScrape):
        crawlerSleeper(i) # we sleep some time in order not to alarm linkedin
        scraped = domainCrawler(driver, elem[1], xpaths)
        bugDetector = incrementBugDetector(scraped[0], bugDetector)
        # If we encounter more than 3 links in a row that return an error we stop the crawling
        if bugDetector >= 3:
            print("We encountered multiple errors")
            driver.quit()
            break
        targetWriter.writerow(elem + scraped)


def mainCrawler(workFiles, xpaths, batchSize = 10):
    '''
    When launched, this function resumes the scraping where it stopped. We probably need to scrape a lot of urls but we can only scrape so much in one shot. That's why the scraping has to stop after a few and resume where it stopped afterwards, until the whole list has been scraped.
    @params: {dict, list, int} the dictionnary with a path to the input csv file with urls to scrape and a path to the file with the linkedin credentials of the account to connect to, the list of xpaths where to get data on each linkedin page and the number of urls to visit in one shot (defaults to 10). Last parameter was designed to not raise linkedin's awareness about our ongoing scraping.
    @returns {None}
    '''
    sourceFileName = workFiles["source"]
    targetFileName = sourceFileName.split(".")[0] + "Result.csv"
    dataSource, targetData = openCSV(sourceFileName, targetFileName) 
    nbToScrape = len(dataSource) 
    nbScraped = len(targetData)

    if nbToScrape == nbScraped:
        print("Everything's already been scraped")
    else:
        with open("./data/" + targetFileName, "a", newline= '') as f1:
            targetWriter = csv.writer(f1)
            if nbScraped == 0:
                targetWriter.writerow(dataSource[0] + len(xpaths)*["column"])
                dataToScrape = dataSource[1:min(1 + batchSize, nbToScrape)]
            else:
                dataToScrape = dataSource[nbScraped:min(nbScraped + batchSize, nbToScrape)]

            scrapedData = domainsCrawler(dataToScrape, xpaths, targetWriter, workFiles["credentials"])       