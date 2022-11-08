#Created: 2022-10-14
#Author: Martin Knudsen
#Purpose: To create svg beizer curves
#V001.000: First version

import ctypes
import random 


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

bdebug = False
xmin = 5
xmax = 70
ymin = 15
ymax = 30
distmax = 60
distmin = 10
svgHeight = 100
svgWidth = 100
svgOutput = "stone.svg"
shape = [[],[]]


# Create shape coordinates
xcord = random.randint(xmin, xmax)
ycord = random.randint(ymin, ymax)

xadd = random.randint(xmin, xmax )
yadd = random.randint(ymin, ymax )

dist = random.randint(distmin, distmax)

#left
shape[0].append([xcord, ycord]) 
shape[0].append([xcord+xadd, ycord+yadd]) 

#right
shape[0].append([xcord+dist-xadd, ycord+yadd]) 
shape[0].append([xcord+dist, ycord])

#top left 
shape[1].append([xcord, ycord]) 
shape[1].append([xcord+xadd, ycord-yadd]) 

#top right
shape[1].append([xcord+dist-xadd, ycord-yadd]) 
shape[1].append([xcord+dist, ycord])

if bdebug: print(shape)


exit
# Create svg file with coordinates
with open(svgOutput , "w") as file:
    
    file.write(f'<svg height=\"{svgHeight}\" width=\"{svgWidth}\" \n')
    file.write('xmlns=\"http://www.w3.org/2000/svg\">\n')

    for i , x in enumerate(shape):
        if bdebug: print(f"X: {x}")

        for z , q in enumerate(x):
            if bdebug: print(f'Z: {z}')
            match z:
                case 0:
                    file.write(f'<path d="M {q[0]} {q[1]} C ')
                case _:    
                    if z != len(q)+1 :
                        file.write(str(q[0]) + " " + str(q[1])  + ", ")
                    else:
                        file.write(str(q[0]) + " " + str(q[1]))
                        file.write('\" ')
                        
                        if i == 0 :
                             file.write(f'fill="black"  stroke="black" />\n')
                        else :
                             file.write(f'fill="black"  stroke="black" />\n')
       

#Circles
    if bdebug:
        for i , x in enumerate(shape):
            for z , q in enumerate(x):
                file.write(f'<circle cx=\"{q[0]}\" cy=\"{q[1]}\" r="2" />')

    file.write('</svg>')

print("Done")