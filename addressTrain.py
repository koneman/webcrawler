import re

addressPossibilities = []

#US address - 19096 Harliegh

#Canadian

#Mexican


#get address/Location
def getAddress (webText):
    address = ""
    #make it more selective picks up onything starting with a number ex 5000 children in Haiti
    #addressCombinations = r'\b\d{1,3}(?:\s[a-zA-Z\u00C0-\u017F]+)+'
    #r'\d+\s?\w+'
    #addressCombinations = r'\d+\s[A-Za-z0-9]+,?\s?[A-Za-z0-9 ]*'

    #{city pattern},[ ](?:{state pattern}|{abbrev. state pattern})[ ]{zip pattern}

    streetNumber = r'\d+'

    streetName = r'[A-Za-z0-9.-]+'

    streetType = r'[A-Za-z0-9.-]+'

    city = r'[A-Za-z0-9.-]+'

    states = r'(AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT \
            |NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY|Alabama|Alaska|\
            Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii| \
            Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|\
            Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New[ ]Hampshire|New[ ]Jersey|New[ ]Mexico|\
            New[ ]York|North[ ]Carolina|North\sDakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode[ ]Island|\
            South[ ]Carolina|South[ ]Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West[ ]Virginia|Wisconsin|Wyoming)'

    zipCode = r'[ ]+(\b\d{5}(?:-\d{4})?\b)?'


    addressCombinations = streetNumber + r'[, ]?\s+' + streetName + r'[, ]?\s+' + streetType + r'[, ]?\s+' + city + r'[, ]?\s*' + states
    #\d{3-10}'
    #r'\d+[ ](?:[A-Za-z0-9.-]+[ ]?)'

    #import pdb; pdb.set_trace()
    comp = re.compile(addressCombinations, re.I )

    address = re.findall(addressCombinations,webText)
    #address = comp.findall("19096  harleigh dr san jose ca 95070")
    print(address)
    return address


getAddress('19096 Harleigh Drive Saratoga, CA 95070')
