import os
import sys
import feedparser
from bs4 import BeautifulSoup
from nltk import clean_html
import urllib


def checkRSSFeed (pageURL):
    isFeedTrue = False

    page = urllib.urlopen(pageURL)
    soup = BeautifulSoup(page, 'html.parser')
    #print soup

    if (soup.find('link', type='application/rss+xml')):
        isFeedTrue = True
        print isFeedTrue
        #rss feed url
        return soup.find('link', type='application/rss+xml')['href']
    else:
        print isFeedTrue

    return isFeedTrue


checkRSSFeed('https://slashdot.org/')
