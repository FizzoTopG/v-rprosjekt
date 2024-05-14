def beregn_score(valgspiller1, valgspiller2):
    if valgspiller1 == "samarbeid" and valgspiller2 == "svik":
        return [0,5]
    elif valgspiller1 == "svik" and valgspiller2 == "samarbeid":
        return [5,0]
    elif valgspiller1 == "svik" and valgspiller2 == "svik":
        return [1,1]
    elif valgspiller1 == "samarbeid" and valgspiller2 == "samarbeid":
        return [3,3]


listy = ["svik", "samarbeid", "svik"]

def spill_snilt(listy):
    antall_svik = listy.count("svik")
    antall_samarbeid = listy.count("samarbeid")

    if antall_svik > antall_samarbeid:
        return "svik"
    else:
        return "samarbeid"
    

    #len(listy) --> gir lengden av lista
    #listy.count("variabel") teller hvor mange ganger variabelen er i lista




def spill_slemt(spill):
    antall = len(spill)
    if antall <= 5:
        return "samarbeid"
    else:
        return "svik"

