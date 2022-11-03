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
amplitude = 40.0
distorsion = 20.0
sinSpan = 0.5
svgHeight = 100
svgWidth = 100
svgOutput = "flowerpic.svg"
shape = []


# Create shape coordinates
i = 0
while i <= points:
    cosVal = math.cos(math.radians(360)/points*i)
    sinVal = math.sin(math.radians(360)/points*i)

    if abs(sinVal) < sinSpan :
        if sinVal >= 0 and cosVal >= 0:
            x = cosVal*amplitude + ((sinSpan-sinVal)*distorsion)
            y = sinVal*amplitude
        elif sinVal <= 0 and cosVal >= 0:
            x = cosVal*amplitude + ((-sinSpan-sinVal)*distorsion*-1.0)
            y = sinVal*amplitude
        elif sinVal >= 0 and cosVal <= 0:
            x = cosVal*amplitude + ((sinSpan-sinVal)*distorsion*-1.0)
            y = sinVal*amplitude
        elif sinVal <= 0 and cosVal <= 0:
            x = cosVal*amplitude + ((-sinSpan-sinVal)*distorsion)
            y = sinVal*amplitude
      
    else:
            x = cosVal*amplitude
            y = sinVal*amplitude         
    
    
    shape.append([x,y])
    i += 1


# Create svg file with coordinates
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\">\n')
    file.write('<polyline points=\"')
    for x in shape:
        file.write(str(x[0]+svgWidth/2) + "," + str( (x[1])+svgHeight/2) + " ")
    
    file.write('\"\n')
    file.write('fill="none" stroke="black" />')
    file.write('</svg>')

print("Done")