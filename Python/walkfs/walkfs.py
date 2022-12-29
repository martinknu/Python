#Walk filesystem to get folder and file info
#Created: 2022-12-25
#Author: Martin Knudsen
#Purpose: Get file and folder info and return object with info

from os import walk
import sys
import json


class FileFolders:
    fileList = []
    fileItem = {
        "name": "name",
        "path": "path",
        "dirname": "dirname",
    }

    #Find PDF files in folder
    def walkFolder(self, folder, searchTopDown, errorHandle, followLinks):
        try:
            for (dirpath, dirnames, filenames) in walk(folder, topdown=searchTopDown, onerror=errorHandle, followlinks=followLinks ):
                for fileName in filenames:
                    self.fileItem['path'] = dirpath 
                    self.fileItem['name'] = fileName 
                    self.fileItem['dirname'] = dirnames
                    self.fileList.append(self.fileItem.copy())
                    self.fileItem.clear
        except:
            print('Error', 'Path does not yield any results, check path or no images in path')   

        #If no files in folder exit 
        if not self.fileList:
            sys.exit("No files found")

        return self.fileList

