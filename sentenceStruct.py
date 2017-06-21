import os
import sys
import feedparser
from bs4 import BeautifulStoneSoup
from bs4 import BeautifulSoup
import nltk
import urllib
import HTMLParser



urlText = []

sentences =''

def ie_preprocess(document):

    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    print sentences
    return sentences

#natural lang
def putIntoLang(inputURL):

    s = inputURL

    ie_preprocess(s)

    tokens = [nltk.tokenize.word_tokenize(s) for u in urlText]
    #print tokens

    grammar = "NP: {<DT>?<JJ>*<NN>}"

    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentences)
    #print result

    result.draw()

#main testing
putIntoLang('Hello, my name is Sathvik. What is your name?')
