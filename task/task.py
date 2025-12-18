from bs4 import BeautifulSoup
import requests

url="https://dunya.com.pk/index.php"
response=requests.get(url)
soup= BeautifulSoup(response.text,"html.parser")

#Quotes= soup.find_all("section", class_= " taza-tareen ")

#for quote in Quotes:

    #heading= quote.find("h5" ,class_="card-title two-line").text
                                        
                                        
#print(Quotes)                                        


#Quotes= soup.find_all("div", class_= " card-body ")

#for quote in Quotes:

    #heading= quote.find("h5" ,class_="card-title two-line").text
                                        
                                        
#print(Quotes)                                        


Quotes= soup.find_all("div", class_= " card-body ")

for quote in Quotes:

    heading= quote.find("a").text
                                        
                                        
print(Quotes)                                        