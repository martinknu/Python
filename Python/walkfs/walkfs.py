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
    def walkFolder(self, folder):
        try:
            for (dirpath, dirnames, filenames) in walk(folder):
                print(filenames)
                self.fileItem['path'] = dirpath 
                self.fileItem['name'] = filenames 
                self.fileItem['dirname'] = dirnames
                self.fileList.append(self.fileItem)
        except:
            print('Error', 'Path does not yield any results, check path or no images in path')   


        #If no files in folder exit 
        if not self.fileList:
            sys.exit("No files found")

        return self.fileList

mywalk = FileFolders()

mysteryFiles= mywalk.walkFolder("folder1")

print(f'mystery files: {mysteryFiles}')
#print(f'mystery files: {mysteryFiles["name"]}')


print(json.dumps(mysteryFiles, indent=4))