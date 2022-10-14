#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To list all jpg files in a folder and create HTML code with the images.
#V001.000: First version

from copy import copy
from os import walk


imgFolder = "/home/martink/sites/python/Python/htmlgenerators/createdivimgs/images"
imgType = ""
filesList = []
imgDict = {"name": "name", "path": "path","desc": "description", "dirpath": "dirpath", "dirnames": "dirnames"}
selList = []
htmlOutput = "htmlpics.txt"


# Walk folder and find all files
for (dirpath, dirnames, filenames) in walk(imgFolder):
    imgDict["name"] = filenames
    imgDict["path"] = dirpath
    imgDict["dirnames"] = dirnames

    print(imgDict)
    filesList.extend(imgDict)

# Filter files for specific type
if imgType == "":
    selList = copy(filesList)
else:
    for x in filesList: 
        if x["name"][-len(imgType):] == imgType:
            #print(x)
            selList.append(x)


#print(selList)

"""
# Create file with images
with open(htmlOutput , "w") as file:

    for x in selList:
        strHTML = "<img style=\"background-color: " + x + " \"> " + x +  " </div>"
        file.write(f'{strHTML}\n')

        """