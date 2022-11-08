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
xmax = 30
ymin = 5
ymax = 30
dist = 50
xcord = 0
ycord = 0
svgHeight = 100
svgWidth = 100
svgOutput = "stone.svg"
shape = [[],[]]


# Create shape coordinates

xcord = 20#random.randint(xmin, xmax)
ycord = 50 #random.randint(ymin, ymax)

print(f'x, ycord: {xcord} , {ycord}')

xadd = 20#random.randint(xmin, xmax )
yadd = 20#random.randint(ymin, ymax )

print(f'x, y add: {xadd} , {yadd}')

#left

shape[0].append([xcord, ycord]) 
shape[0].append([xcord+xadd, ycord+yadd]) 

#right
shape[0].append([xcord+dist, ycord])
shape[0].append([xcord+dist-xadd, ycord+yadd]) 

#top left 
shape[1].append([xcord, ycord]) 
shape[1].append([xcord+xadd, ycord-yadd]) 

#top right
shape[1].append([xcord+dist, ycord-yadd])
shape[1].append([xcord+dist-xadd, ycord-yadd]) 

print(shape)


exit
# Create svg file with coordinates
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\" \n')
    file.write('xmlns=\"http://www.w3.org/2000/svg\">\n')

    for i , x in enumerate(shape):
        print(f"X: {x}")
        for z , q in enumerate(x):
            print(z)
            if z == 0:
                file.write(f'<path d="M {xcord} {ycord} C ')

            if z != len(q) :
                file.write(str(q[0]) + " " + str(q[1])  + ", ")
            else:
                file.write(str(q[0]) + " " + str(q[1]))

            if z == len(q):
                file.write('\" ')
                file.write('fill="none" stroke="black" />\n')

        #else:
            #file.write(str(x[0]) + " " + str(x[1]))           

    file.write('</svg>')

print("Done")