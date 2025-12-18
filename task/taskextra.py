from bs4 import BeautifulSoup
import requests
import json


url="https://quotes.toscrape.com/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")



Quotes= soup.find_all("div", class_="quote")

for q in Quotes:

    link= "\n""  https://quotes.toscrape.com" + q.find("a") ["href"]
    #print(link)
    url=link
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    detail=soup.find_all("div", class_="author-details")
    for d in detail:
        name=d.find("h3", class_="author-title").text
        #print(name)
        description=d.find("div", class_="author-description").text
        #print(description)



with open('data123.json', 'w') as file:
    json.dump(, file, indent=4)