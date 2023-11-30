# creëer hier de gevraagde functie(s) met implementatie:

def ggd(eerstegetal,tweedegetal):
    while eerstegetal != tweedegetal:
        if eerstegetal < tweedegetal:
            if tweedegetal-eerstegetal > 0:
                tweedegetal -= eerstegetal
            else:
                break
        else:
            if eerstegetal-tweedegetal > 0:
                eerstegetal -= tweedegetal
            else:
                break
    for x in range(1,eerstegetal):
        if eerstegetal/x == tweedegetal:
            return eerstegetal/x

# testen:
assert ggd(12, 18) == 6
assert ggd(5, 25) == 5
assert ggd(75, 165) == 15