import geograpy


e = extraction.Extractor(url='http://www.bbc.com/news/world-europe-26919928')
e.find_entities()

# You can now access all of the places found by the Extractor
print e.places
