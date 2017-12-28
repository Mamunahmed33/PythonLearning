import requests
from bs4 import BeautifulSoup

def spider(url):
    sourceCode = requests.get(url)
    plainText = sourceCode.content

   # print(plainText)

    soup = BeautifulSoup(plainText, "html.parser")

    fw = open("C:\\Users\\User\\Desktop\\a.txt", "wb")

    h2 = soup.findAll('h2', {"class": "story-heading"})

    for l in h2:
        a = l.find("a")
        if a:
            href = a.get("href")
            #print(href)

            innerLink = requests.get(href)
            innerContent = innerLink.content
            #print(innerContent)
            innerSoup = BeautifulSoup(innerContent, "html.parser")

            for c in innerSoup.find_all(["h1", "p"]):
                print(c.text)

#spider("http://www.trans-pro.com.au/")
spider("https://www.nytimes.com/")