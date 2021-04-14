import time
import random as rd

def sleepShortTime():
    """Program sleeps for a random time between 2s and 5s"""
    sleepTime = rd.uniform(2,5)
    time.sleep(sleepTime)

def sleepLongTime():
    """Program sleeps for a random time between 20s and 40s"""
    sleepTime = rd.uniform(20,40)
    time.sleep(sleepTime)

def sleepVeryLongTime():
    """Program sleeps for a random time between 8 and 12 minutes"""
    sleepTime = rd.uniform(480,720)
    time.sleep(sleepTime)

def crawlerSleeper(counter):
    '''
    Depending on a counter value (in our case the number of urls processed in one shot), we sleep for some time.
    @params: {int}, the counter
    @returns: {None}
    '''
    if counter % 10 == 5:
        sleepLongTime()
    elif counter % 20 == 0 and counter > 0:
        sleepVeryLongTime()
    else:
        sleepShortTime()

def incrementBugDetector(scrapingRes, bugDetector):
    '''
    If the input evaluates to "error", then we increment the other input. The point being to raise a flag when the incremented value reaches a certain threshhold (but that happens elsewhere)
    @params: {str, int} the value to evaluate, the value to increment depending on the case.
    @returns {int} the incremented (or not) bugDetector
    '''
    if scrapingRes == "error":
        bugDetector += 1
    else:
        bugDetector = 0
    return bugDetector