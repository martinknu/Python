from walkfs import FileFolders
import json


#Example useage
mywalk = FileFolders()
mysteryFiles= mywalk.walkFolder("C:/Users/n1mmkk/Dalux/NP_HVVP/Files/Building/D2 Aflevering/DV", True, None, True)

#print(f'mystery files: {mysteryFiles}')
print(json.dumps(mysteryFiles, indent=4))

