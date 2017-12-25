import requests
from bs4 import BeautifulSoup
import operator

def wordList(url):
    wordList = []

    sourceCode = requests.get(url)
    plainText = sourceCode.text

    soup = BeautifulSoup(plainText, "html.parser")

    for articleText in soup.find_all("p", {"class": "story-body-text story-content"}):
        content = articleText.string
        if content:
            word = content.lower().split()

        for eachWord in word:
            if eachWord:
                wordList.append(eachWord)
                #print(eachWord)

    cleanUpList(wordList)
    printListEleents(wordList)


def cleanUpList(wordList):
    cleanWordList = []
    symbols = "'~!@#$%^&*(){}[]?<>\"/;:-"
    for word in wordList:
        for i in range(0, len(word)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            cleanWordList.append(word)

    printListEleents(cleanUpList())

def printListEleents(list):
    print(list)
    for i in range(0, len(list)):
        print(list[i])

wordList("https://www.nytimes.com/2017/12/24/us/politics/congress-2017-conservative-courts-taxes-trump.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news")
