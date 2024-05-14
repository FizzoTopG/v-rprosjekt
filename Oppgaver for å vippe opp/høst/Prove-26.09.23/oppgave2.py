dato = input("Skriv in bursdagen in i ISO-format (YYYY-MM-DD): ")

år, mnd, dato = dato.split("-") # splitter opp stengen der hvor "-" er

print("Bursdagsdatoen din ser slik ut i norsk standard:" ,dato + "." + mnd + "." + år + ".")
