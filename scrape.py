import requests
from bs4 import BeautifulSoup
import json as jas
import pandas as pd
import os as os
import csv

#Connect to site 
page = requests.get("https://espc.com/house-prices/edinburgh?ps=50")
soup = BeautifulSoup(page.content, 'html.parser')

#Retrive Json
scripts = soup.find_all('script')
j = str(scripts[15])
j1 = j.split('<script>\r\n            var initialProps = ')
j2 = j1[1]
j3 = j2.split(';\r\n        </script')
string = j3[0]

#Beautify
json = jas.loads(string)

properties = json['properties']
final = jas.dumps(properties, indent=4, sort_keys=True)

#Save JSON file 
jsonFile = open('edin50.json', 'w+')
jsonFile.write(str(final))




#Save as csv file
#df = pd.json_normalize(jsonFile)
#df.to_csv('edin50.csv', index=False, sep='\t', encoding='utf-8')

jsonFile.close()