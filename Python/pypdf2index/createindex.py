#Created: 2022-11-17
#Author : Martinknu
#Purpose: To join several PDF documents and insert breaker pages with document information, and create index with ref to all breaker pages.

#Imports
from PyPDF2 import PdfWriter
from PyPDF2._page import PageObject
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


#Function - create annotation
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


#Declerations
writer = PdfWriter()
output = open("breakerpages.pdf", "wb")
breakerwidth = 595
breakerheight = 842


#Create pages and outlines
for il1 in range(0,6):

    #Add annotations showing page numbers
    myAnnDict = free_text(
        text=f'Page: {il1+1}',
        rect=(breakerwidth/2-100, breakerheight/2+100, breakerwidth/2+100, breakerheight/2-100+100), #Left, bottom, right, top
        font="helvetica",
        bold=True,
        italic=True,
        font_size="60pt",
        font_color="FFFFFF",
        border_color="000000",
        background_color="10FFC2"
    )    

    # Add new page and the data
    newpage = PageObject().create_blank_page(pdf=None, width=breakerwidth,height=breakerheight)
    writer.add_page(newpage)
    writer.add_annotation(page_number=il1, annotation=myAnnDict)
    writer.add_outline_item(f'Outline Item page : {il1+1}', page_number=il1, color="800080")
    writer.write(output)
output.close()