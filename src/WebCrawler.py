import requests
from bs4 import BeautifulSoup

def spider():
    url = "http://www.prothom-alo.com/"
    sourceCode = requests.get(url)
    plainText = sourceCode.text

    soup = BeautifulSoup(plainText, "html.parser")

    fw = open("C:\\Users\\User\\Desktop\\a.txt", "wb")

    for link in soup.find_all('a', {"class": "link_overlay"}):
        href = "http://www.prothom-alo.com/" + link.get("href")
        print(href)

        innerSource = requests.get(href)
        innerText = innerSource.text
        soup1 = BeautifulSoup(innerText, "html.parser")

        for pText in soup1.find_all(["p", "h1"]):
            if pText.string:
                print(pText.string)
       # for pText in soup1.find_all("p", {"class": "TEXT"}):
        #    print(pText.string)
            #if pText:fw.write(pText.string.encode('utf8'))
            #fw.write(pText.string.encode("utf-8"))


    fw.close()



spider()