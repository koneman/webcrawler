import nltk
from urllib import urlopen

url = "https://achildshopefoundation.org/endeavors/haiti"
html = urlopen(url).read()
raw = nltk.clean_html(html)
print(raw)
