import requests
from bs4 import BeautifulSoup

block_to_match = "blockquote"

url = "https://studentcouncil.dk/organisations/connect"
s = requests.get(url).content.decode("utf-8")

soup = BeautifulSoup(s, features="lxml")

print(soup.find(block_to_match))
print()
print(soup.find(block_to_match).text)