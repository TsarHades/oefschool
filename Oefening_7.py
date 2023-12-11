# vereenvoudig dubbele code, splits op in aparte functie(s):
def gemiddelde_van_tekst(getaltekst1: str, getaltekst2: str) -> str:
    return f'{gemiddelde(getaltekst1)} : {gemiddelde(getaltekst2)}'

def gemiddelde(getal:str) -> str:
        getaltekst = getal
        teller: int = 0
        som: int = 0
        while teller < len(getaltekst):
            som += int(getaltekst[teller])
            teller += 1
        gemiddeldeuit: float = som / len(getaltekst)

        return gemiddeldeuit


# testen:
assert gemiddelde_van_tekst("1234", "5678") == "2.5 : 6.5"
assert gemiddelde_van_tekst("5678", "1234") == "6.5 : 2.5"
