#intro 
logget_inn = False

if logget_inn:
    print("Velkommen!")
else:
    print("Logg inn!")

# Tester

## Sammenligningsoperatorer
# > # verdien til venstre er større enn den til høyre
# >= # veriden til venstre er strørre enn eller lik verdien til høyre
# < # verdien til høyre er større enn den til venstre
# <= # veriden til høyre er strørre enn eller lik verdien til venstre
# == # Tester om verdiene er like. lik. Hvis dette er sant får vi ut "True", hvis ikke "false"
# != # Tester om verdiene IKKE er like. ikke lik. Hvis de er ulike får vi ut "True", hvis de er like så "false"

print( 3 != 2)
resultatet_av_test = 42 == 12
print(resultatet_av_test)

# Logiske operatorer
alder = 71
yrke = "lærer"

alder > 70 and yrke == "lærer" # -> true
alder < 70 or yrke == "lærer" # -> false + true = true
not alder > 70 # -> False