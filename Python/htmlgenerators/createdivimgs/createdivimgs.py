#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To list all jpg files in a folder and create HTML code with the images.
#V001.000: First version

import os
from copy import copy
from os import walk
import ctypes 
import sys


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


imgFolder = "images2"
wwwFolder = "images2/"
imgType = ""
imgWidth = "600"
divClass = "image_gallery"
filesList = []
imgDict = {"name": "", "path": "","size": ""} 
selList = []
htmlOutput = "htmlpics.txt"



# Walk folder and find all files
try:
    for (dirpath, dirnames, filenames) in walk(imgFolder):
        filesList.extend(filenames)
except:
    Mbox('Error', 'Path does not yield any results, check path or no images in path', 1)   


if not filesList:
    sys.exit("No files found")


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
        file.write("<div class=\"" + divClass + "\">\n")
        strHTML = "<img src=\"" + wwwFolder + x["name"] + "\" alt=\"" + x["name"] + "\" width=\"" + imgWidth + "\"  style=\"display: block; margin:10px; border-radius: 15px\" >"
        file.write(f'{strHTML}\n')
        file.write("</div>\n")
