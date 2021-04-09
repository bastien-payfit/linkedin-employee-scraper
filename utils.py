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
    if counter % 10 == 5:
        sleepLongTime()
    if counter % 100 == 0 and counter > 0:
        sleepVeryLongTime()

def incrementBugDetector(scrapingRes, bugDetector):
    if scrapingRes == "error":
        bugDetector += 1
    else:
        bugDetector = 0