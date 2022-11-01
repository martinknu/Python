#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To create svg from math expression sinodial curve
#V001.000: First version

import ctypes
import math 


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)



points = 500
amplitude = 5.0
svgHeight = 100
svgWidth = 1000
svgOutput = "sinodialpic.svg"
shape = []


# Create shape
i = 0
while i <= points:
    #print(i)
    #print(math.sin(i))
    shape.append([svgWidth/points*i,  math.sin(math.radians(360)/points*i)])
    i += 1



# Create svg
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\">\n')
    file.write('<polyline points=\"')
    for x in shape:
        print(x)
        file.write(str(x[0]) + "," + str((svgHeight/2) + (x[1])* amplitude) + " ")
    
    file.write(f'{svgWidth},{svgHeight/2} ')
    file.write(f'{svgWidth},{svgHeight} ')
    file.write(f'0,{svgHeight} ')
    #file.write(f'0,{svgHeight/2}')
    file.write('\"\n')
    file.write('fill="black" stroke="black" />')
    file.write('</svg>')
