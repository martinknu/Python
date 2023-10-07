#Created: 2023-10-06
#Author: Martin Knudsen
#Purpose: To create svg with random circles around a central circle
#V001.000: First version

import ctypes
import math 
import random


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


circles = random.randint(3, 9)
radiusMain = 30
svgHeight = 100
svgWidth = 100
svgOutput = "randomcircles.svg"
shape = []
shapeColors = ["red", "yellow", "green", "blue", "cyan", "purple", "orange", "magenta", "white", "black"]

# Create shape coordinates
i = 0
while i <= circles:   
    radiusMinor = random.randint(int(radiusMain/6), int(radiusMain/2))
    shape.append([random.randint(radiusMinor , svgWidth - radiusMinor ), random.randint(radiusMinor , svgHeight - radiusMinor ), radiusMinor, shapeColors[min(i,len(shapeColors))] ])
    i += 1

print(shape)
# Create svg file with coordinates
i = 0
with open(svgOutput , "w") as file:

    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\" \n')
    file.write('xmlns=\"http://www.w3.org/2000/svg\">\n')

    file.write('<circle cx="' + str(svgWidth/2) + '" cy="' + str( svgHeight/2) + '" r="' + str(radiusMain) + '" fill="' + shapeColors[1] + '" stroke="black"  />\n')

    file.write('\n')
    for x in shape:
        file.write('<circle cx="' + str(x[0]) + '" cy="' + str( x[1]) + '" r="' + str(x[2]) + '" fill="' + shapeColors[i] + '" stroke="black"  />\n')
        i += 1    
    file.write('\"\n')
    file.write('fill="blue" stroke="black" />')
    file.write('</svg>')

print("Done")