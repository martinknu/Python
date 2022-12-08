#Created: 2022-11-17
#Author : Martinknu
#Purpose: To join several PDF documents and insert breaker pages with document information, and create index with ref to all breaker pages.

#Imports
from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2._page import PageObject
from PyPDF2.generic import AnnotationBuilder
from PyPDF2.generic._data_structures import DictionaryObject, ArrayObject
from PyPDF2.generic._rectangle import RectangleObject
from PyPDF2.generic._utils import hex_to_rgb
from PyPDF2.generic._base import (
    BooleanObject,
    FloatObject,
    NameObject,
    NullObject,
    NumberObject,
    TextStringObject,
)
from typing import Optional, Tuple, Union
from os import walk
import ctypes
import sys


#Function to create annotation
def free_text(
    text: str,
    rect: Union[RectangleObject, Tuple[float, float, float, float]],
    font: str = "Times",
    bold: bool = False,
    italic: bool = False,
    font_size: str = "60pt",
    font_color: str = "000000",
    border_color: str = "000000",
    background_color: str = "ffffff",
) -> DictionaryObject:
    font_str = "font: "
    if bold is True:
        font_str = font_str + "bold "
    if italic is True:
        font_str = font_str + "italic "
    font_str = font_str + font + " " + font_size
    font_str = font_str + ";text-align:center;color:#" + font_color

    bg_color_str = ""
    for st in hex_to_rgb(border_color):
        bg_color_str = bg_color_str + str(st) + " "
    bg_color_str = bg_color_str + "rg"

    free_text = DictionaryObject()
    free_text.update(
        {
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/FreeText"),
            NameObject("/Rect"): RectangleObject(rect),
            NameObject("/Contents"): TextStringObject(text),
            # font size color
            NameObject("/DS"): TextStringObject(font_str),
            # border color
            NameObject("/DA"): TextStringObject(bg_color_str),
            # background color
            NameObject("/C"): ArrayObject(
                [FloatObject(n) for n in hex_to_rgb(background_color)]
            ),
        }
    )
    return free_text


# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


#Declerations
merger = PdfMerger()
mergerlist = []
mergerlistlength = []
mergerobjects = []
metadatalist = []
breakerpages = []
sourcefolder = "docs"
writer = PdfWriter()
output = open("breakerpages.pdf", "wb")
breakerwidth = 595
breakerheight = 842



myAnnDict = DictionaryObject

#Find PDF files in folder
try:
    for (dirpath, dirnames, filenames) in walk(sourcefolder):
        #print(f'Dir path: {dirpath}')
        mergerlist.extend(filenames)
        #print(f'Filenames list: {filenames}')
except:
    Mbox('Error', 'Path does not yield any results, check path or no images in path', 1)   


#If no files in folder exit 
if not mergerlist:
    sys.exit("No files found")


#Get metadata from PDFs in mergerlist
for pdf in mergerlist:
    reader = PdfReader(sourcefolder + "/" + pdf)
    mergerobjects.append(reader.pages)
    mergerlistlength.append(len(reader.pages))
    meta = reader.metadata
    metadatalist.append(meta)
    #print(f'Metadata: {metadatalist[len(metadatalist)-1]}')
    #print('\n')
print(mergerobjects)
#print(f'Document length: {mergerlistlength}')


#Create breaker pages
il1 = 0
for pdffile in mergerlist:
    
    myAnnDict = free_text(
        text=f'{pdffile}',
        rect=(breakerwidth/2-100, breakerheight/2+100, breakerwidth/2+100, breakerheight/2-100+100), #Left, bottom, right, top
        font="helvetica",
        bold=True,
        italic=True,
        font_size="60pt",
        font_color="FFFFFF",
        border_color="000000",
        background_color="FFFFFF"
    )

    # Add the line
    annotation = AnnotationBuilder.link(
        rect=(50, 150, 200, 250), target_page_index=1, fit="/FitH", fit_args=(123,)
    )


    newpage = PageObject().create_blank_page(pdf=None, width=breakerwidth,height=breakerheight)
    writer.add_page(newpage)
    writer.add_annotation(page_number=il1, annotation=myAnnDict)
    writer.add_annotation(page_number=il1, annotation=annotation)

    #writer.add_page(mergerobjects[il1])
    writer.write(output)
    il1 += 1

#Create index
writer.add_outline_item(
    title=f'This is the outline item to insert as index',
    page_number=0,
    parent=None,
    color="FFFFFF",
    bold=False,
    italic=False,
    fit="/Fit"
)


output.close()

#write merge documents
input1 = open("breakerpages.pdf", "rb")
for il1 in range(0,len(mergerlist)):
    print(il1)
    merger.append(fileobj=input1, pages=(il1, il1+1))
    merger.append(sourcefolder + "/" + mergerlist[il1])




merger.write("merged-pdfs.pdf")
merger.close()
