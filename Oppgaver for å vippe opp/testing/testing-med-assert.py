# assert 3 > 2 # sjekk at 3 er større enn 2
# assert 2 > 3 # gir en feilmeldning, koden stopper

# Test-drevet utvikling med assert

## Eksempel en funskjon som tester om tall er partall
def partall(tall: int):
    if tall % 2== 0:
        return True
    if tall == 1:
        return False

# assert gir feilmelding hvis noe ikke funker
assert partall(2) == True, "2 er et partall"
assert partall(1) == False
assert partall(-2) == True
assert partall(-1) == False