import os
import sys
import feedparser
from bs4 import BeautifulStoneSoup
from bs4 import BeautifulSoup
import nltk
import urllib
import re

#using consec nouns to find address
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

#using alg
def getAddress(webText):


        streetNumber = r'\d+'
        state = r'(AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT \
                |NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY \
                Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii| \
                Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|\
                Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New[ ]Hampshire|New[ ]Jersey|New[ ]Mexico|\
                New[ ]York|North[ ]Carolina|North[ ]Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode[ ]Island|\
                South[ ]Carolina|South[ ]Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West[ ]Virginia|Wisconsin|Wyoming)'
        zipCode = r'[ ]+(\b\d{5}(?:-\d{4})?\b)'


        addressBenchmark = state + zipCode

        #find address
        address = re.findall(addressBenchmark, webText)
        print address

        stringReform = ''
        index = 0
        addressList = ['','']
        #append string
        for (a,b) in address:
            stringReform = a + ' ' + b
            addressList[index] = re.sub("^u'(.*)'$",r'\1',stringReform)
            index += 1

        #print addresses
        print addressList

        #find position of zipcode
        for x in addressList:
            numberEndLoc = webText.find(x) + len(x) + 1

            #print (webText.find(streetNum))

            #assign starting point for looking for street number
            startSearch = numberEndLoc - 55

            neededText = webText[startSearch:numberEndLoc]

            #print neededText
            street_number = re.findall(streetNumber,neededText)

            print street_number

            addressStart = []
            for s in street_number:
                addressStart.append(neededText.find(s))

            print addressStart
            print neededText[addressStart[0]:-1]

            addressData = []
            addFinal = ''
            for a in addressStart:
                addFinal = neededText[a:]
                print(addFinal)
                addressData.append(addFinal)

        print addressData



url = 'https://achildshopefoundation.org/endeavors/haiti'
HTMLtext = getHTMLtext(url)

#address
getAddress(HTMLtext)
