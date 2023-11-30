# creëer hier de gevraagde functie(s) met implementatie:
def vervang_tekst(zoekterm,woord,vervangterm):
    if zoekterm in woord:
        woordsplit = woord.split(zoekterm)
        print(woordsplit)
        woordstuff = woord.split(zoekterm)[0] + vervangterm + woord.split(zoekterm)[1]
        if "" in woordsplit:
            woordstuff = woordstuff + vervangterm + woord.[1]
            print(woordstuff)


# testen:
#assert vervang_tekst("ee", "computationeel denken", "aa") == "computationaal denken"
assert vervang_tekst("ten", "hottentottententententoonstelling",
                     "stuff") == "hotstufftotstuffstuffstuffstufftoonstelling"
assert vervang_tekst("e", "ee", "ee") == "eeee"
assert vervang_tekst("e", "eee", "eee") == "eeeeeeeee"