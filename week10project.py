import requests

from bs4 import BeautifulSoup

r = requests.get("https://nces.ed.gov/programs/digest/d19/tables/dt19_204.20.asp")
soup = BeautifulSoup(r.text)

elltable = soup.find("div-class"== "nces")
#print(elltable)
elldata = elltable.findAll("tr")
#print(elldata)

completeelldata=[[2000, 2005, 2010, 2014, 2015, 2016, 2017, 2000, 2005, 2010, 2014, 2015, 2016, 2017]]

for i in elldata[7:-7]:
    cleanelldata=list(i.stripped_strings)
    completeelldata.append(cleanelldata)
print(completeelldata)
