# Created 2023-09-06
# Read file with RDS names and make dict with all the names
 

# Declerations
file1 = open('rdsnames.txt', 'r')
rdsNames = { }


 #Begin code
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    strippedLine = line.replace('\n','')
    strippedLine = strippedLine.replace('=','',1)
    lineSplit = strippedLine.split("=")
 
    lengthSplit = len(lineSplit)


    if lengthSplit >= 1:
        if not lineSplit[0] in rdsNames:
            rdsNames[lineSplit[0]] = {}

    if lengthSplit >= 2:
        if not lineSplit[1] in rdsNames[lineSplit[0]]:
            rdsNames[lineSplit[0]][lineSplit[1]]  = {}

    if lengthSplit >= 3:
        if not lineSplit[2] in rdsNames[lineSplit[0]][lineSplit[1]]:
            rdsNames[lineSplit[0]][lineSplit[1]][lineSplit[2]]   = {}


    if lengthSplit >= 4:
        if not lineSplit[3] in rdsNames[lineSplit[0]][lineSplit[1]][lineSplit[2]]:
            rdsNames[lineSplit[0]][lineSplit[1]][lineSplit[2]][lineSplit[3]]   = {}


#Output to file
fileOutput = open("RDSOutput.txt", "w")

for key1 in rdsNames:
    print(key1)
    fileOutput.write(key1 + '\n')
    if len(rdsNames[key1]) >=1:
        for key2 in rdsNames[key1]:
            print(key2)
            fileOutput.write('  ' + key2 + '\n')
            if len(rdsNames[key1][key2]) >=1:
                for key3 in rdsNames[key1][key2]:
                    print(key3)
                    fileOutput.write('      ' + key3 + '\n')
                    if len(rdsNames[key1][key2][key3]) >=1:
                        for key4 in rdsNames[key1][key2][key3]:
                            print(key4)
                            fileOutput.write('          ' + key4 + '\n')



fileOutput.close()


#print(rdsNames)