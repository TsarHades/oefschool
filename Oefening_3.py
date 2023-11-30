# creëer hier de gevraagde functie(s) met implementatie:
def verwerk_commando(commando):
    if "vermenigvuldigen" in commando:
        getal1 = float(commando.split(" ")[1])
        getal2 = float(commando.split(" ")[2])
        return getal2*getal1
    if "aftrekken" in commando:
        getal1 = float(commando.split(" ")[1])
        getal2 = float(commando.split(" ")[2])
        return getal1-getal2
    if "optellen" in commando:
        getal1 = float(commando.split(" ")[1])
        getal2 = float(commando.split(" ")[2])
        return getal1 + getal2
    if "delen" in commando:
        getal1 = float(commando.split(" ")[1])
        getal2 = float(commando.split(" ")[2])
        return getal1/getal2

# testen:
assert verwerk_commando("optellen 5.7 6.3") == 12.0
assert verwerk_commando("optellen -5 10") == 5
assert verwerk_commando("optellen 10 -5") == verwerk_commando("optellen -5 10")
assert verwerk_commando("aftrekken -55.5 55.2") == -110.7
assert verwerk_commando("aftrekken 10 5") == 5
assert verwerk_commando("aftrekken 5 10") == -verwerk_commando("aftrekken 10 5")
assert verwerk_commando("vermenigvuldigen 24 3") == 72
assert verwerk_commando("vermenigvuldigen 15.2 6.8") == 103.36
assert verwerk_commando("vermenigvuldigen 6.8 15.2") == verwerk_commando("vermenigvuldigen 15.2 6.8")
assert verwerk_commando("delen 125 5") == 25
assert verwerk_commando("delen 144.6 8") == 18.075
assert verwerk_commando("delen 8 144.6") == 1 / verwerk_commando("delen 144.6 8")