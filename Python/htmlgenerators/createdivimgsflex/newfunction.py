def creatediv(**kwargs):
    '''
    Created HTML code with a div and embedded image or divs.

    Args:
        htmlfile (string): file to output HTML code. 
    
    kwargs: 
        divId, divClass, divText
        divImage{imgClass, imgSrc, imgAlt}.
    
    return:
        strdiv (string)
    '''


    strdiv = "<div "

    if "divId" in kwargs:
        strdiv = strdiv + "id=\"" + kwargs.get("divId") + "\""

    if "divClass" in kwargs:
        strdiv = strdiv + " class=\"" + kwargs.get("divClass")

    strdiv = strdiv + "\"> "

    if "divText" in kwargs:
        strdiv = strdiv + kwargs.get("divText")

    if "embedImage" in kwargs:
        for divImage in kwargs.get("embedImage"):
            strdiv = strdiv + "<img"
            if "imgClass" in divImage:
                strdiv = strdiv + " class=\""  + divImage["imgClass"] + "\""  
            if "imgSrc" in divImage:
                strdiv = strdiv + " src=\""  + divImage["imgSrc"] + "\""  
            if "imgAlt" in divImage:
                strdiv = strdiv + " alt=\""  + divImage["imgAlt"] + "\""  
            strdiv = strdiv + ">"

    if "embedDiv" in kwargs:
        for embeddedDiv in kwargs.get("embedDiv"):
            print(embeddedDiv)
            strdiv = strdiv + creatediv(**embeddedDiv)

    strdiv = strdiv + " </div>"
    print(strdiv)

    #with open(htmlfile , "a") as file:
    #    file.write(strdiv + "\n")

    return strdiv
creatediv(divId="some_id", divClass="some_class", divText="my text to insert", embedImage=[{"imgClass": "someimageclass", "imgSrc": "images2/ash-edmonds-oQ7Y1cU-Rlg-unsplash.jpg", "imgAlt": "alt text"},{"imgClass": "someimageclass", "imgSrc": "images2/ash-edmonds-oQ7Y1cU-Rlg-unsplash.jpg", "imgAlt": "alt text"}], embedDiv=[{"divId": "embeddeddivid1", "divClass": "embeddeddivclass1"},{"divId": "embeddeddivid2", "divClass": "embeddeddivclass2"}])