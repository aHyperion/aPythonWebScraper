from bs4 import BeautifulSoup
import requests
import sys

def scrap():
    pageToScrape = requests.get(url)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    authors = soup.findAll(tag, attrs ={'class':tagClass})

    for author in authors:
        print(author.text)

url = sys.argv[1]
tag = sys.argv[2]
tagClass = sys.argv[3]
scrap()