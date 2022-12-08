#Created: 2022-11-17
#Author : Martinknu
#Purpose: To test PdfWriter

#Imports
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
import ctypes


#Function to create annotation
def free_text(
    text: str,
    rect: Union[RectangleObject, Tuple[float, float, float, float]],
    font: str = "Times",
    bold: bool = False,
    italic: bool = False,
    font_size: str = "30pt",
    font_color: str = "000000",
    border_color: str = "000000",
    background_color: str = "ffffff",
) -> DictionaryObject:
    """
    Add text in a rectangle to a page.

    :param str text: Text to be added
    :param RectangleObject rect: or array of four integers
        specifying the clickable rectangular area ``[xLL, yLL, xUR, yUR]``
    :param str font: Name of the Font, e.g. 'Helvetica'
    :param bool bold: Print the text in bold
    :param bool italic: Print the text in italic
    :param str font_size: How big the text will be, e.g. '14pt'
    :param str font_color: Hex-string for the color
    :param str border_color: Hex-string for the border color
    :param str background_color: Hex-string for the background of the annotation
    """
    font_str = "font: "
    if bold is True:
        font_str = font_str + "bold "
    if italic is True:
        font_str = font_str + "italic "
    font_str = font_str + font + " " + font_size
    font_str = font_str + ";text-align:right;color:#" + font_color

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
mypage = PageObject().create_blank_page(pdf=None, width=1680,height=1050)
mystr = "String object"
#print(mypage)

myAnnDict = DictionaryObject
print(f'My own annotation dict: {myAnnDict}')




#Write breakerpages with metadata
writer = PdfWriter()
output = open("breakerPage.pdf", "wb")
#writer.add_blank_page(1680,1050)
writer.add_page(mypage)
# Create the annotation

myAnnDict = free_text(
    text="Automatic inserted annotation\nThis is the second line!\nBut this time from other function",
    rect=(500, 550, 1180, 1000),
    font="Times",
    bold=True,
    italic=False,
    font_size="30pt",
    font_color="000000",
    border_color="000000",
    background_color="C2C2C2"
)


#annotation = AnnotationBuilder.free_text(
#    text="Automatic inserted annotation\nThis is the second line!",
#    rect=(500, 550, 1180, 1000),
#    font="Helvetica",
#    bold=True,
#    italic=False,
#    font_size="30pt",
#    font_color="000000",
#    border_color="000000",
#    background_color="C2C2C2",
#)
#print(annotation)
#if "text-align" in annotation["/DS"]:
#    print("the key is there")




#annotation["text-align"] = "center"
#print(f'Annotation object: {annotation}')

#print(f'Annotation keys: {annotation.keys()}')

#print(f'Examine typeof: {type(annotation)}')
#Exit prematurely
#exit()

#print(annotation["/DS"])
#print(type(annotation["/DS"]))


writer.add_annotation(page_number=0, annotation=myAnnDict)

print(f'Pages: {writer.getNumPages()}')

writer.write(output)
output.close


