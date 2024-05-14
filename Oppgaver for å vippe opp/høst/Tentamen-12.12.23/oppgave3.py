# 3.1 Penger per stream

def per_stream(land: str):
    if land == "Norge":
        return 0.55
    if land == "Sverige":
        return 0.44
    if land == "Finland":
        return 0.44
    if land == "Danmark":
        return 0.52
    if land == "Island":
        return 0.62
    else:
        return 0.24

# print(per_stream("Norge"))
# print(per_stream("Island"))
# print(per_stream("USA"))


# 3.2 - Penger tjent på spotify

def andel_til_artist(antall_streams: int):
    if antall_streams >= 0 and antall_streams <= 399_999:
        return 0
    if antall_streams >= 1_400_00 and antall_streams <= 29_999_999:
        return 0.40
    if antall_streams >= 30_000_000:
        return 0.70
    
# print(andel_til_artist(50_00))
# print(andel_til_artist(5_000_000))
# print(andel_til_artist(50_000_000))


# 3.3 - Penger tjent

def penger_tjent(antall_streams, land: str):
    return antall_streams * per_stream(land) * andel_til_artist(antall_streams)

# print(penger_tjent(5_000_000, "Norge"))
# print(penger_tjent(100_000_000, "Island"))


# 3.4 - Populære artister

def populære(artistliste):
    ny_liste = []
    for artist in artistliste:
        if artist[1] > 100_000_000:
            ny_liste.append(artist)
    return ny_liste

    
artister = [
        ["Taylor Swift", 109_940_000],
        ["The Weeknd", 105_410_000],
        ["Justin Bieber", 83_820_000],
        ["Drake", 81_980_000],
        ["Ariana Grande", 81_800_000]
        ]

# print(populære(artister))


# 3.5 - Royalties

def royalties(artistliste):
    ny_liste = []
    for profit in artistliste:
        print(profit[0], penger_tjent(profit[2],profit[1]))

artister1 = [
    ["Sigur Ros", "Island", 1_047_010],
    ["Emma Steinbakken", "Norge", 3_459_239]
    ]

print(royalties(artister1))

