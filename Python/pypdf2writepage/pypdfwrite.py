#Created: 2022-11-17
#Author : Martinknu
#Purpose: To test PdfWriter

#Imports
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2.generic import AnnotationBuilder

from PyPDF2._page import PageObject

import ctypes

# Messagebox
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


#Declerations
mypage = PageObject().create_blank_page(pdf=None, width=1680,height=1050)
mystr = "String object"
print(mypage)


#Write breakerpages with metadata
writer = PdfWriter()
output = open("breakerPage.pdf", "wb")
#writer.add_blank_page(1680,1050)
writer.add_page(mypage)
# Add the annotation
annotation = AnnotationBuilder.free_text(
    text="Automatic inserted annotation\nThis is the second line!",
    rect=(500, 550, 1180, 1000),
    font="Helvetica",
    bold=True,
    italic=False,
    font_size="30pt",
    font_color="000000",
    border_color="000000",
    background_color="C2C2C2",
)
#print(annotation)
if "text-align" in annotation:
    print("the key is there")


#annotation["text-align"] = "center"
print(f'Annotation object: {annotation}')

print(f'Annotation keys: {annotation.keys()}')

print(f'Examine typeof: {type(annotation)}')

#annotation["/DS"] = "font: bold Helvetica 14pt;text-align:center;color:#000000"
print(annotation["/DS"])
print(type(annotation["/DS"]))


writer.add_annotation(page_number=0, annotation=annotation)

print(f'Pages: {writer.getNumPages()}')

writer.write(output)
output.close


