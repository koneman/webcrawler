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

def nltkPractice (webText):
    tokenizedText = nltk.word_tokenize(webText)

    POStagged = nltk.pos_tag(tokenizedText)

    #print(POStagged)
    #get all nouns

    wordLength = range(len(POStagged)-1)

    for x in wordLength:
        word = POStagged[x]
        consecutive_word = POStagged[x+1]
        if word[1] == consecutive_word[1]:
            nounList = word[1] + consecutive_word[1]
            print "Noun: ", word, consecutive_word
            print nounList
            


url = 'https://achildshopefoundation.org/endeavors/haiti'
HTMLtext = getHTMLtext(url)
#GetAddresses(url)

#print(HTMLtext)

#phone
getPhoneNumber(HTMLtext)

#email
getEmail(HTMLtext)

#address
nltkPractice(HTMLtext)
