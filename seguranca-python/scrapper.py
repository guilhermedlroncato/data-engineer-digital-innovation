from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br").content

soup = BeautifulSoup(site, 'html.parser')

temperatura = soup.find("span", class_ = "city _margin-r-5 -font-13")

#print(soup.prettify())
print(temperatura)