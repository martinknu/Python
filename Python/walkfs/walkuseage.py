from walkfs import FileFolders
import json


#Example useage
mywalk = FileFolders()
mysteryFiles= mywalk.walkFolder("./testfolder", True, None, True)

#print(f'mystery files: {mysteryFiles}')
print(json.dumps(mysteryFiles, indent=4))

