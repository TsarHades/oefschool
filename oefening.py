maximum = int(input("Welke waarde mogen de veelvouden maximum hebben?"))
startwaarde: int=0
for deelbaar in range(0,maximum):
    if deelbaar%5 == 0 or deelbaar%3 == 0:
        startwaarde += deelbaar
print(startwaarde)
