# Creatediv
def creatediv(htmlfile, **kwargs):

    strdiv = "<div "

    if "divId" in kwargs:
        strdiv = strdiv + "id=\"" + kwargs.get("divId") + "\""

    if "divClass" in kwargs:
        strdiv = strdiv + " class=\"" + kwargs.get("divClass")

    strdiv = strdiv + "\"> "

    if "divImage" in kwargs:
        divImage = kwargs.get("divImage")
        strdiv = strdiv + "<img"
        if "imgclass" in divImage:
            strdiv = strdiv + " class=\""  + divImage["imgclass"] + "\""  
        if "imgsrc" in divImage:
            strdiv = strdiv + " src=\""  + divImage["imgsrc"] + "\""  
        if "imgalt" in divImage:
            strdiv = strdiv + " alt=\""  + divImage["imgalt"] + "\""  
        strdiv = strdiv + ">"

    strdiv = strdiv + " </div>"
    print(strdiv)

    with open(htmlfile , "w") as file:
        file.write("</div>\n")

creatediv("myfile", divId="some_id", divClass="some_class", divImage={"imgclass": "someclass", "imgsrc": "imagesource", "imgalt": "alt text"})