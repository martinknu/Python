#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To create svg from math expression sin but in vase mode 
#V001.000: First version

import ctypes
import math 


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


points = 1000
amplitude = 5.0
svgHeight = 100
svgWidth = 1000
svgOutput = "vasepic.svg"
shape = []


# Create shape coordinates
i = 0
while i <= points:
    shape.append([svgWidth/points*i,  math.sin(math.radians(360)/points*i)])
    i += 1


# Create svg file with coordinates
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\">\n')
    file.write('<polyline points=\"')

    for x in shape:
        file.write(str(x[0]) + "," + str((svgHeight/4) + (x[1])* amplitude) + " ")

    for x in reversed(shape):
        file.write(str(x[0]) + "," + str((svgHeight/4*3) + (x[1])* amplitude * -1) + " ")

    file.write(f'0,{svgHeight/4} ')
    file.write('\"\n')
    file.write('fill="black" stroke="black" />')
    file.write('</svg>')

print("Done")