import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.request


r = urllib.request.urlopen("https://www.imdb.com/title/tt7638344/").read()

soup = BeautifulSoup(r, 'html.parser')

table=soup.find("table", attrs={"class":"cast_list"})
cstr = "DHARAK MOVIE"
print ("")
print (cstr.center(60, "#"))

for tr in table('tr'):
    row = [t.get_text(strip=True) for t in tr(['td', 'th'])]

    print("\n")
    for i in row:
        if (i !='...'):
            print(i, end="    ")
