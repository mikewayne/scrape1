#From YP.com, scraping using 1st video lecture on YT by CFE.
#https://www.youtube.com/watch?v=3xQTJi2tqgk&list=PLEsfXFp6DpzR6FatOy4RtoXfu4PeYO_RL

import requests
from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=tutoring&geo_location_terms=98682"
url2 = url + "&page=2"
url3 = url + "&page=3"

r = requests.get(url)
r2 = requests.get(url2)
r3 = requests.get(url3)

soup = BeautifulSoup(r.content, "lxml")
soup2 = BeautifulSoup(r2.content, "lxml")
soup3 = BeautifulSoup(r3.content, "lxml")

links = soup.find_all("a")
links2 = soup2.find_all("a")
links3 = soup3.find_all("a")

for link in links:
    print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

for link in links2:
    print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

for link in links3:
    print "<a href='%s'>%s</a>" %(link.get("href"), link.text)        

g_data = soup.find_all("div", {"class": "info"})
g_data2 = soup2.find_all("div", {"class": "info"})
g_data3 = soup3.find_all("div", {"class": "info"})

#for item in g_data:
#    print item.text

for item in g_data: 
    
    try:
        print item.contents[0].find_all("a", {"class": "business-name"})[0].text
    except:
        pass    

    try:
        print item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
    except:
        pass
    #address_locality =     
    try:
        print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
    except:
        pass        
    try:
        print item.contents[1].find_all("li", {"class": "primary"})[0].text
    except:
        pass  

for item in g_data2: 
    
    try:
        print item.contents[0].find_all("a", {"class": "business-name"})[0].text
    except:
        pass    

    try:
        print item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
    except:
        pass
    #address_locality =     
    try:
        print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
    except:
        pass        
    try:
        print item.contents[1].find_all("li", {"class": "primary"})[0].text
    except:
        pass  

for item in g_data3: 
    
    try:
        print item.contents[0].find_all("a", {"class": "business-name"})[0].text
    except:
        pass    

    try:
        print item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
    except:
        pass
    #address_locality =     
    try:
        print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
    except:
        pass        
    try:
        print item.contents[1].find_all("li", {"class": "primary"})[0].text
    except:
        pass  

