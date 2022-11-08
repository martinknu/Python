#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To create svg from math expression sinodial curve by beizer curve
#V001.000: First version

import ctypes
import math 


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

bdebug = True
amplitude = 20
svgHeight = 100
svgWidth = 100
svgOutput = "sinodialpicbeizer.svg"
shape = [[],[]]
colors = ["red", "orange", "yellow", "green", "purple", "cyan", "magenta", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]


# Create shape coordinates
shape[0].append([0,math.floor(svgHeight/2)])
shape[0].append([math.floor(svgWidth/6) ,  math.floor(svgHeight/2+amplitude)])
shape[0].append([math.floor(svgWidth/6*2), math.floor(svgHeight/2+amplitude)])
shape[0].append([math.floor(svgWidth/6*3) ,math.floor( svgHeight/2)])
shape[1].append([math.floor(svgWidth/6*3) , math.floor(svgHeight/2)])
shape[1].append([math.floor(svgWidth/6*4) , math.floor(svgHeight/2-amplitude)])
shape[1].append([math.floor(svgWidth/6*5) , math.floor(svgHeight/2-amplitude)])
shape[1].append([math.floor(svgWidth), math.floor(svgHeight/2)])


# Create svg file with coordinates
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\" \n')
    file.write('xmlns=\"http://www.w3.org/2000/svg\">\n')

    for i, x in enumerate(shape):
        for z, q in enumerate(x):
            match z:
                case 0:
                    file.write(f'<path d="M {q[0]} {q[1]} C ')
                case _:    
                    if i != len(x) :
                        file.write(f'{q[0]} {q[1]}, ')
                    else:
                        file.write(f'{q[0]} {q[1]}')
        file.write(f'" fill="none" stroke="black" />\n')


#Debug points
    if bdebug:
        for i , x in enumerate(shape):
            for z , q in enumerate(x):
                file.write(f'<circle cx=\"{q[0]}\" cy=\"{q[1]}\" r="2" stroke="{colors[z+(i*len(q))]}" />\n')



    file.write('</svg>')

print("Done")