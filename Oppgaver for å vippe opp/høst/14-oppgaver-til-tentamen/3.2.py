def pris_inkl_frakt(varepris):
    if varepris > 1000:
        return varepris
    
    if varepris >= 500 and varepris <= 1000:
        return varepris + 50
    
    if varepris < 500:
        return varepris + 80
    
print(pris_inkl_frakt(300))
print(pris_inkl_frakt(600))
print(pris_inkl_frakt(1300))