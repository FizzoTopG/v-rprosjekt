# Simulering av troskapstesten i Paradise hotell

def main():
    pott = 0
    print("velkommen Til Troskapstesten")
    for i in range(10):
        pott = pott + 10000
        print(f"Runde {i + 1}: {pott},-") # plus 1 fordi da starten den på 1 og slutter på 10 
        if not snill_spiller(pott) == False:
            print("Snill spiller kastet kula")
            break
        elif not scpellar(pott) == False: 
            print("spellaren kastet kula")
            break

        


def snill_spiller(beløp):
    return True # beholder kula 

def slem_spiller(beløp):
    return False #Kaster kula

def scpellar(beløp):
    if beløp >= 30000:
        return False
    else:
        return True

main()