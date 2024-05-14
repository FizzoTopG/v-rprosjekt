# Program for reisekarantene

def karantene(vaksinert, farge):
    if vaksinert:
        return 0
    elif vaksinert == False and (farge == "rød" or farge == "oransj"):
        return 10
    elif vaksinert == False and farge == "grønn":
        return 3

print(karantene(True, "rødx"))