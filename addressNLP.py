import os
import sys
import feedparser
from bs4 import BeautifulStoneSoup
from bs4 import BeautifulSoup
import nltk
import urllib
import re


#getting all text on a page
def getHTMLtext (url):
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    HTMLtext = soup.get_text()
    return HTMLtext

def findConsecNouns(inputText):

        #all the nouns in the middle
        tokenizedText = nltk.word_tokenize(inputText)

        POStagged = nltk.pos_tag(tokenizedText)

        #print(POStagged)
        #get all nouns
        wordLength = range(len(POStagged)-1)
        nounList = ''

        for x in wordLength:
            #word = POStagged[x]
            #consecutive_word = POStagged[x+1]
            if POStagged[x][1] == POStagged[x+1][1]:
                nounList += POStagged[x][0] + POStagged[x+1][0]
                #print "Noun: ", POStagged[x][0], POStagged[x+1][0]
        #print nounList


def nltkPractice (webText):

    streetNumber = r'\d+'
    #address = re.compile(streetNumber)
    address = re.findall(streetNumber, webText)
    numberList = []

    for number in address:
        numberList.append(number)

    #for number in address.finditer(webText):
    #    location.append(number.end())
    """
    numberEndLoc = webText.find('165') + 4
    neededText = webText[numberEndLoc:]
    print neededText
    """

    for number in numberList:
        numberEndLoc = webText.find(number) + len(number) + 1
        neededText = webText[numberEndLoc:]
        #print neededText


url = 'https://achildshopefoundation.org'
HTMLtext = getHTMLtext(url)
#GetAddresses(url)


#address
nltkPractice(HTMLtext)
