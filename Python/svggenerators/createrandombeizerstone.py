#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To create svg beizer curves
#V001.000: First version

import ctypes
import random 


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

xmin = 5
xmax = 95
ymin = 5
ymax = 95
dist = 50
xcord = 0
ycord = 0
svgHeight = 100
svgWidth = 100
svgOutput = "stone.svg"
shape = []


# Create shape coordinates

xcord = random.randint(xmin, xmax)
ycord = random.randint(ymin, ymax)


shape.append([xcord, ycord]) 

xadd = random.randint(-xmin, xmin)
yadd = random.randint(-ymin, ymin)
shape.append([xcord+xadd, ycord+yadd]) 


xadd = random.randint(-xmin, xmin)
yadd = random.randint(-ymin, ymin)
shape.append([xcord+xadd, ycord+yadd]) 


# Create svg file with coordinates
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\" \n')
    file.write('xmlns=\"http://www.w3.org/2000/svg\">\n')
    file.write(f'<path d="M {xcord} {ycord} C ')
    for i , x in enumerate(shape):
        if i != len(shape) - 1:
            file.write(str(x[0]) + " " + str(x[1])  + ", ")
        else:
            file.write(str(x[0]) + " " + str(x[1]))           
    file.write('\"\n')
    file.write('fill="black" stroke="black" />')
    file.write('</svg>')

print("Done")