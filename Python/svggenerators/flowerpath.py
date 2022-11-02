#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To create svg from math expression circle
#V001.000: First version

import ctypes
import math 


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


points = 500
radius = 5.0
amplitude = 50.0
svgHeight = 100
svgWidth = 100
svgOutput = "flowerpic.svg"
shape = []


# Create shape coordinates
i = 0
while i <= points:
    x = math.sin(math.radians(360)/points*i)*amplitude + math.sin(math.radians(360)/points*i)* 3
    y = math.cos(math.radians(360)/points*i)*amplitude + math.cos(math.radians(360)/points*i) * 3
    shape.append([x,y])
    i += 1


# Create svg file with coordinates
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\">\n')
    file.write('<polyline points=\"')
    for x in shape:
        file.write(str(x[0]+svgWidth/2) + "," + str( (x[1])+svgHeight/2) + " ")
    
    #file.write(f'{svgWidth},{svgHeight/2} ')
    #file.write(f'{svgWidth},{svgHeight} ')
    #file.write(f'0,{svgHeight} ')
    file.write('\"\n')
    file.write('fill="none" stroke="black" />')
    file.write('</svg>')

print("Done")