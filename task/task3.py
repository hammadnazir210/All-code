from bs4 import BeautifulSoup
import requests
import csv

url="https://quotes.toscrape.com/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")



with open("task3.csv","w", newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow([" Quote " , " Link "])

    Quotes= soup.find_all("div", class_="quote")

    for qùotes in Quotes:

        Text= q.find("span", class_="text").text


        link= "\n""  https://quotes.toscrape.com" + q.find("a") ["href"]



        writer.writerow([Text , link ])
