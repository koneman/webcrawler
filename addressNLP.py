import os
import sys
import feedparser
from bs4 import BeautifulStoneSoup
from bs4 import BeautifulSoup
import nltk
import urllib
import re

<<<<<<< HEAD
#using consec nouns to find addresses
=======
#using consec nouns to find address
>>>>>>> a4f1f3cfbadecfb1519c05975d3e2646ccadb3b4
#getting all text on a page
def getHTMLtext (url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    HTMLtext = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in HTMLtext.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    HTMLtext = '\n'.join(chunk for chunk in chunks if chunk)

    return HTMLtext

def findConsecNouns(inputText):

        #all the nouns in the middle
        tokenizedText = nltk.word_tokenize(inputText)

        POStagged = nltk.pos_tag(tokenizedText)

        #accepted nltk POS tags - NN, NNP, nouns
        wordLength = range(len(POStagged)-1)
        nounList = ''
        word = r'[A-Za-z]+\s'
        firstPart = r'\s'

        for x in wordLength:
            if (POStagged[x][1] and POStagged[x+1][1]) in ['NN','NNP','NNS']:
                nounList += POStagged[x][0] + POStagged[x+1][0]
                #print "Noun: ", POStagged[x][0], POStagged[x+1][0]
        print nounList


def nltkPractice (webText):

    streetNumber = r'\d+ '
    #address = re.compile(streetNumber)
    address = re.findall(streetNumber, webText)

    #for number in address.finditer(webText):
    #    location.append(number.end())
    """
    numberEndLoc = webText.find('165') + 4
    neededText = webText[numberEndLoc:]
    print neededText
    """

    for number in address:
        numberEndLoc = webText.find(number) + len(number)
        neededText = webText[numberEndLoc:]
        print number
        findConsecNouns(neededText)
        #print neededText


url = 'https://achildshopefoundation.org'
HTMLtext = getHTMLtext(url)
#print HTMLtext
#GetAddresses(url)


#address
nltkPractice(HTMLtext)
