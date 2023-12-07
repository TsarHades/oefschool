# creëer hier de gevraagde functie(s) met implementatie:
def aantal_keren_voorkomen(lijst):
    lijst.sort()
    print(lijst)
    x = 1
    check = []
    for i in range(0, len(lijst)-1):
        if lijst[i] == lijst[i+1]:
            x += 1
        else:
            check.append((lijst[i], int(x)))
            x = 1
    check.append((lijst[len(lijst)-1], int(x)))
    print(check)
    return check


# testen:
assert aantal_keren_voorkomen(["a", "b", "c", "b", "c", "b", "a"]) == [("a", 2), ("b", 3), ("c", 2)]
assert aantal_keren_voorkomen(["c", "b", "a", "a", "b", "c", "b"]) == [("a", 2), ("b", 3), ("c", 2)]
assert aantal_keren_voorkomen([1, 4, 2, 3, 2, 9, 1]) == [(1, 2), (2, 2), (3, 1), (4, 1), (9, 1)]
