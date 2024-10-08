
def getRating(ratingHtml):
    
    if ratingHtml != None:
        return ratingHtml.text()
    else:
        return 0