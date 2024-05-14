temp = float(input("Hva er kroppstemperaturen din? "))

if temp < 36.5:
    print("Tempereturen din ligger under normal temperatur! Du er litt kald..")
elif temp > 37.5:
    print("Temperaturen din er over normal temperatur! Du er muligens litt syk")
elif temp >= 36.5:
    print("Tempereturen din ligger henholdvis til normal temperatur! Du er frisk")
elif temp <= 37.5:
    print("Tempereturen din ligger henholdvis til normal temperatur! Du er frisk")