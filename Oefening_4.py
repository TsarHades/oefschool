# creëer hier de gevraagde functie(s) met implementatie:
def vervang_tekst(zoekterm,woord,vervangterm):
    woordeind = woord
    woordsplit2 = woord
    while zoekterm in woordsplit2:
        woordsplit = woordeind.split(zoekterm)[0]
        print(woordsplit)
        woordsplit2 = woordeind.split(woordsplit + zoekterm)[1]
        print(woordsplit2)
        woordeind = woordsplit + vervangterm + woordsplit2
        print(woordeind)
    return woordeind


# testen:
assert vervang_tekst("ee", "computationeel denken", "aa") == "computationaal denken"
assert vervang_tekst("ten", "hottentottententententoonstelling",
                     "stuff") == "hotstufftotstuffstuffstuffstufftoonstelling"
assert vervang_tekst("e", "ee", "ee") == "eeee"
assert vervang_tekst("e", "eee", "eee") == "eeeeeeeee"
