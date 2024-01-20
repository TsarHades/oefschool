# creëer hier de gevraagde functie(s) met implementatie:
def is_perfect_getal(getal):
    som = 0
    for i in range(1,getal):
            if getal%i == 0:
                som+=i
    if som == getal:
        return True
    else:
        return False
# testen:
assert is_perfect_getal(6)
assert is_perfect_getal(496)
assert not is_perfect_getal(35)