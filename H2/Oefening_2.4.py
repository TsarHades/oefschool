# creëer hier de gevraagde functie(s) met implementatie:

def vervang_tekst(zoekterm, woord, vervangterm):
    for i in range(0, len(woord)):
        if zoekterm in woord[i:i+len(zoekterm)]:
            print(zoekterm[i:len(zoekterm)])
            print(woord)
            woord = woord[:i] + vervangterm + woord[i+len(zoekterm):]
    print(woord)
    return woord


# testen:
assert vervang_tekst("ee", "computationeel denken", "aa") == "computationaal denken"
assert (vervang_tekst("ten", "hottentottententententoonstelling", "stuff") ==
        "hotstufftotstuffstuffstuffstufftoonstelling")
assert vervang_tekst("e", "ee", "ee") == "eeee"
assert vervang_tekst("e", "eee", "eee") == "eeeeeeeee"
