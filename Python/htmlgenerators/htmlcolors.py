

colorFile = "colors.txt"
finalList = []



#File open within with statement
with open(colorFile , "r") as file:
    ##content = file.read()
    colorNames = file.readlines()
   ## colorNames = colorNames.split(",")
file.close


for y in colorNames:
    print("The content is:")
    print(y[:-1])
    finalList.append(y[:-1])

#------------ create files---------------
with open("allcolorshtml.txt" , "a") as file:

    for x in finalList:
        strHTML = "<div style=\"background-color: " + x + " \"> " + x +  " </div>"
        file.write(f'{strHTML}\n')

 