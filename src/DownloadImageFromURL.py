import random
import urllib.request

def downloadImage(url):
    name = random.randrange(0, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

downloadImage('type the url.jpg here')