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
           # print(word)
        for eachWord in word:
            if eachWord:
                wordList.append(eachWord)
                #print(eachWord)

    cleanUpList(wordList)
   # printListEleents(wordList)


def cleanUpList(wordList):
    cleanWordList = []
    symbols = "'~!@#$%^&*(){}[]?<>\`\";:-,_."
    for word in wordList:
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            cleanWordList.append(word)

   # printListEleents(cleanUpList())
    createDictionary(cleanWordList);

def createDictionary(cleanWordList):
    wordCount = {}

    for word in cleanWordList:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    for key, value in sorted(wordCount.items(), key = operator.itemgetter(1)):
        print(key, value)


def printListEleents(list):
    print(list)
    for i in range(0, len(list)):
        print(list[i])

wordList("https://www.nytimes.com/2017/12/24/us/politics/congress-2017-conservative-courts-taxes-trump.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news")
