from skuff import Skuff
from sokker import Sokk


def hovedprogram():
    sokken_leif = Sokk("V")
    sokken_luff = Sokk("H")
    skuffen = Skuff()

    skuffen.sett_inn_sokk(sokken_luff)
    skuffen.sett_inn_sokk(sokken_luff)
    skuffen.sett_inn_sokk(sokken_leif)
    skuffen.sett_inn_sokk(sokken_leif)
    skuffen.sjekk_status()
    skuffen.sett_inn_sokk(Sokk("V"))
    skuffen.sjekk_status()

hovedprogram()