from app import db, ELLTable
import requests

from bs4 import BeautifulSoup 
    
# set up your scraping below
r = requests.get("https://nces.ed.gov/programs/digest/d19/tables/dt19_204.20.asp")
soup = BeautifulSoup(r.text,features="html.parser")
elltable = soup.find("div-class"== "nces")
#print(elltable)
toremove=elltable.findAll('sup')
for x in toremove:
    x.extract()
elldata = elltable.findAll("tr")
#print(elldata)

completeelldata=[]
for i in elldata[7:-7]:
    cleanelldata=list(i.stripped_strings)
    completeelldata.append(cleanelldata)
completeelldata

# this `main` function should run your scraping when 
# this script is ran.
def main():
    db.drop_all()
    db.create_all()
    for row in completeelldata:
        if len(row)==0:
            continue
        newrow=ELLTable(location=row[0],number_2000=row[1],number_2005=row[2],number_2010=row[3],number_2014=row[4],number_2015=row[5],number_2016=row[6],number_2017=row[7],percent_2000=row[8],percent_2005=row[9],percent_2010=row[10],percent_2014=row[11],percent_2015=row[12],percent_2016=row[13],percent_2017=row[14])
        db.session.add(newrow)
        db.session.commit()
    # for key,val in rows.items():
    #     new_row = DBTable(column_1=key, column_2=val)
    #     print(new_row)
    #     db.session.add(new_row)
    #     db.session.commit()
    
        

if __name__ == '__main__':
    main()