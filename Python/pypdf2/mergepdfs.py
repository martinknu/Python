#Created: 2022-11-17
#Author : Martinknu
#Purpose: To join several PDF documents and insert breaker pages with document information

#Imports
from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2.generic import AnnotationBuilder
from os import walk
import ctypes
import sys

# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


#Declerations
merger = PdfMerger()
mergerlist = []
sourcefolder = "docs"
dictannotation = {
    "key": "value",
    "key2": "value2",
}

#Find PDF files in folder
try:
    for (dirpath, dirnames, filenames) in walk(sourcefolder):
        print(f'Dir path: {dirpath}')
        mergerlist.extend(filenames)
except:
    Mbox('Error', 'Path does not yield any results, check path or no images in path', 1)   


if not mergerlist:
    sys.exit("No files found")


#Get metadata from PDFs
il1 = 1 
for pdf in mergerlist:
    reader = PdfReader(sourcefolder + "/" + pdf)

    meta = reader.metadata

    print(f'Pages: {len(reader.pages)}')

    # All of the following could be None!
    print(f'Author: {meta.author}')
    print(f'Producer: {meta.producer}')
    print(f'Creator: {meta.creator}')
    print(f'Subject: {meta.subject}')
    print(f'Title: {meta.title}')

    #Write breakerpages with metadata
    writer = PdfWriter()
    output = open("breakerPage_" + str(il1) + ".pdf", "wb")
    writer.add_blank_page(1680,1050)
    # Add the line
    annotation = AnnotationBuilder.free_text(
        "Hello World\nThis is the second line!",
        rect=(50, 550, 200, 650),
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
    )
    writer.add_annotation(page_number=0, annotation=annotation)

    print(f'Pages: {writer.getNumPages()}')

    #writer.add_annotation(writer.getNumPages(), "Annotation")
    writer.write(output)
    #print(f'Writer: {writer}')
    output.close
    #writer.add_blank_page(100,200)
    il1 += 1


    #Merge PDF
    merger.append(sourcefolder + "/" + pdf)
    print(f'merging: {pdf}')

merger.write("merged-pdf.pdf")
merger.close()


