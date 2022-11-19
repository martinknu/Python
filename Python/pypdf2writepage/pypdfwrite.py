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
print(mypage)


#Write breakerpages with metadata
writer = PdfWriter()
output = open("breakerPage.pdf", "wb")
#writer.add_blank_page(1680,1050)
writer.add_page(mypage)
# Add the annotation
annotation = AnnotationBuilder.free_text(
    "Automatic inserted annotation\nThis is the second line!",
    rect=(0, 0, 1680, 1050),
    font="Arial",
    bold=True,
    italic=False,
    font_size="3pt",
    font_color="000000",
    border_color="000000",
    background_color="FFFFFF",
)
writer.add_annotation(page_number=0, annotation=annotation)

print(f'Pages: {writer.getNumPages()}')

writer.write(output)
output.close


