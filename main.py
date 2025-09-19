#lightshot requires two letters and 4 numbers in front of it
#save it in an image folder

import requests
import re
import random
from PIL import Image


payload = {}
files={}
lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36"
}

def urlGeneration():
    number = random.randint(1000,9999)
    randomNum1 = random.randint(0,25)
    randomNum2 = random.randint(0,25)
    urlWord = "https://prnt.sc/"+lettersList[randomNum1] + lettersList[randomNum2] + str(number)
    return urlWord

def getContent():
    url = urlGeneration()
    response = requests.request("GET", url, headers=headers)
    if(response.status_code!=200):
        print("unable to access server")
    else:
        with open("file.txt","wb") as f:
            f.write(response.content)
            f.close()
    getImageUrl()

def getImageUrl():
    with open("file.txt","+rt") as f:
        text = f.read()
        urlList = re.findall(r'<meta\s+property="og:image"\s+content="([^"]+)"', text)
        url = urlList[0]
        getImage(url)


def getImage(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36"
    }
    imageRequest = requests.request("GET",url,headers=headers)
    #this can stop the pictures that dont work and only produce a picture with an actual picture
    if(imageRequest.status_code!=200):
        getContent()
    else:
        with open("image.png","wb") as image:
            image.write(imageRequest.content)
            im = Image.open("image.png")
            im.show()

if __name__ == "__main__":
    getContent()

