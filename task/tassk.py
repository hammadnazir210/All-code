from bs4 import BeautifulSoup
import requests

url="https://quotes.toscrape.com/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")


Quotes=soup.find_all("div", class_="quote")

for q in Quotes:
    name=q.find("div", class_="tags").text
    print(name)