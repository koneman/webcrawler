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

#get the phone number on webpage with regex
def getPhoneNumber (webText):
    phoneNumber = ""

    phoneNumberCombinations = r'\(?\d?-?\d{,3}?\)?\s?\.?-?/?\(?\d{3}\)??\s?\.?-?/?\d{3}\s?\.?-?\d{4}'

    #catch index out of range error
    phoneNumber = re.findall(phoneNumberCombinations, webText)[0]

    #print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}',webText))
    #basic case
    """
    phoneNumberCombos = [r'\(?\d{3}\)? \d{3}-\d{4}', r'\(?\d{3}\)?.?\d{3}.?\d{4}']
    for numbers in phoneNumberCombos:
        phoneNumber = re.findall(numbers, webText)
        print(phoneNumber)
    """
    print(phoneNumber)
    return phoneNumber


#get email
def getEmail (webText):
    email = ""
    #basic case
    emailCombinations = r'[-\w\d+.]+@[-\w\d.]+'

    #catch index out of range error
    email = re.findall(emailCombinations, webText)[0]
    print(email)
    return email

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

#print(HTMLtext)

#phone
getPhoneNumber(HTMLtext)

#email
getEmail(HTMLtext)

#address
nltkPractice(HTMLtext)
