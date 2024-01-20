# creëer hier de gevraagde functie(s) met implementatie:
def aantal_keren_voorkomen(gezocht_getal,zoeklijst):
    counter = 0
    for i in range(0,len(zoeklijst)):
        if zoeklijst[i] == gezocht_getal:
            counter+=1
    return counter


# testen:
assert aantal_keren_voorkomen(20, ()) == 0
assert aantal_keren_voorkomen(20, (9, 6, 11, 99)) == 0
assert aantal_keren_voorkomen(20, (1, 6, 20, 88)) == 1
assert aantal_keren_voorkomen(20, (20, 10, 20, 100, 20)) == 3