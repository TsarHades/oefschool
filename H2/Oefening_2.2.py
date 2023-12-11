# creëer hier de gevraagde functie(s) met implementatie:
def aantal_keren_voorkomen(gezocht, woord):
    aantalwoord = 0
    for aantal in range(0, len(woord)):
        if woord[aantal] == gezocht:
            aantalwoord += 1
    return aantalwoord


def heeft_hetzelfde_aantal(gezochte, woord1, woord2):
    if aantal_keren_voorkomen(gezochte, woord1) == aantal_keren_voorkomen(gezochte, woord2):
        return True
    else:
        return False


# testen:
assert aantal_keren_voorkomen("t", "hottentottententententoonstelling") == 10
assert aantal_keren_voorkomen("a", "python") == 0

assert heeft_hetzelfde_aantal("e", "computer", "lopen") == True
assert heeft_hetzelfde_aantal("o", "python", "toledo") == False
# opmerking: deze 2 laatste asserties kunnen eventueel nog korter geschreven worden naar:
# assert heeft_hetzelfde_aantal("e", "computer", "lopen")
# assert not heeft_hetzelfde_aantal("o", "python", "toledo")
