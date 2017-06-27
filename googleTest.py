
import os
import sys
import feedparser
from bs4 import BeautifulStoneSoup
from bs4 import BeautifulSoup
from nltk import clean_html
import urllib
import re


#getting all text on a page
def getHTMLtext (url):
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    HTMLtext = soup.get_text()
    return HTMLtext



url = 'https://www.google.com/search?q=childs+hope+foundation&oq=childs+hope+foundation&aqs=chrome..69i57j0l5.5973j0j7&sourceid=chrome&ie=UTF-8'
HTMLtext = getHTMLtext(url)

print HTMLtext
