#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To list all jpg files in a folder and create HTML code with the images.
#V001.000: First version

import os
from copy import copy
from os import walk


imgFolder = "/home/martink/sites/python/Python/htmlgenerators/createdivimgs/images"
wwwFolder = "media/"
imgType = ""
filesList = []
imgDict = {"name": "", "path": "","size": ""} 
selList = []
htmlOutput = "htmlpics.txt"


# Walk folder and find all files
for (dirpath, dirnames, filenames) in walk(imgFolder):
    filesList.extend(filenames)

# Filter files for specific type and get additional info
for x in filesList:
    if x[-len(imgType):] == imgType or imgType == "":
        fileInfo = os.stat(imgFolder + "/" + x)
        imgDict["name"] = x
        imgDict["path"] = imgFolder + "/" + x
        imgDict["size"] = fileInfo.st_size

        imgDictCopy = imgDict.copy()
        selList.append(imgDictCopy)


# Create file with images
with open(htmlOutput , "w") as file:

    for x in selList:
        strHTML = "<img src=\"" + wwwFolder + x["name"] + "\" alt=\"" + x["name"] + "\" width=\"500\"  style=\"display: block; margin:10px; border-radius: 15px\" >"
        file.write(f'{strHTML}\n')


# height=\"600\"