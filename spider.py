"""
Stuff to scrap:
most important: Website, Email, Phone,Name,
Location of headquarters, Project, Name, Description of project

next level stuff nltk: Project budget, Project partners,Specialisations
Past projects, Ongoing projects, Project proposals

reminders TO DO: start focusing on scrapping entire webpages
- check out scrapy later - if contact us is seperate link
also convert to JSON data and create skeleton API service
"""

import os
import sys
import feedparser
from bs4 import BeautifulStoneSoup
from bs4 import BeautifulSoup
from nltk import clean_html
import urllib
import re



def cleanHtml(html):
    return BeautifulStoneSoup(clean_html(html),
                              convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]


#parse link
def get_feedparser_feed(FEED_URL):

    fp = feedparser.parse(FEED_URL)

    #fp = feedparser.parse('https://achildshopefoundation.org/endeavors/haiti')
    #need to check if link is legit + if it has rss
    #if rss ez parse if not nltk

    if ('title') in fp.feed:
            print "Fetched %s entries from %s" % (len(fp.entries), fp.feed.title)
    else:
        print 'No RSS feed!'
        sys.exit()
    return fp


#checks for rss feed in a webpage - returns rss feed if true else null
def checkRSSFeed (inputURL):
    isFeedTrue = False

    page = urllib.urlopen(inputURL)
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


#for rss feeds
def rssScraper(pageURL):

    global feed_dict, form_data

    rssURL = checkRSSFeed(pageURL)
    parsedRSS = get_feedparser_feed(rssURL)
    form_data = []


    if parsedRSS:
        feed_dict = {'title': parsedRSS.feed.title,
                     'content': parsedRSS.feed.description,
                     'link': parsedRSS.feed.link}
        form_data.append(feed_dict)
    print form_data

    return form_data

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

#get address/Location
def getAddress (webText):
    address = ""
    #make it more selective picks up onything starting with a number ex 5000 children in Haiti
    #addressCombinations = r'\b\d{1,3}(?:\s[a-zA-Z\u00C0-\u017F]+)+'
    #r'\d+\s?\w+'
    #addressCombinations = r'\d+\s[A-Za-z0-9]+,?\s?[A-Za-z0-9 ]*'

    #{city pattern},[ ](?:{state pattern}|{abbrev. state pattern})[ ]{zip pattern}

    street = r'\d+[ ]+(?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?,?[ ]+(?:[A-Za-z0-9.-]+[ ]?)+'
    stateAbbrev = r'(AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT \
            |NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)?'
    state = r'(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii| \
            Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|\
            Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New[ ]Hampshire|New[ ]Jersey|New[ ]Mexico|\
            New[ ]York|North[ ]Carolina|North[ ]Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode[ ]Island|\
            South[ ]Carolina|South[ ]Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West[ ]Virginia|Wisconsin|Wyoming)?'
    zipCode = r'[ ]+(\b\d{5}(?:-\d{4})?\b)?'


    addressCombinations = street + state + stateAbbrev + zipCode
    #\d{3-10}'
    #r'\d+[ ](?:[A-Za-z0-9.-]+[ ]?)'

    #import pdb; pdb.set_trace()
    comp = re.compile(addressCombinations, re.I )

    #address = re.findall(addressCombinations,webText)
    address = comp.findall('19096 harleigh drive saratoga, ca 95070')
    print(address)
    return address



#test
#p = cleanHtml('https://achildshopefoundation.org/endeavors/haiti')
#print p



url = 'https://achildshopefoundation.org/endeavors/haiti'
HTMLtext = getHTMLtext(url)
#GetAddresses(url)

#print(HTMLtext)

#phone
getPhoneNumber(HTMLtext)

#email
getEmail(HTMLtext)

#address
getAddress(HTMLtext)

#check if rss feed exists to scrap that good stuff
if checkRSSFeed(url):
    rssScraper(url)
