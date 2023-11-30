print("Welkom bij dit programma om temperatuurseenheden om te zetten. Gemaakt door Nicolas Jacobs.")
print("Mogelijke opties: Celsius, Fahrenheit, Kelvin")
testl: str = ""
while testl == "":
    van = input("In welke eenheid staan je graden nu? ")
    vanl = van.lower()
    if "c" in vanl[0]:
        naar = input("Naar welke eenheid wil je omzetten? ")
        naarl = naar.lower()
        if "c" in naarl[0]:
            eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
            print(eenheid, "°C", " => ", eenheid, "°C", sep="")
        else:
            if "k" in naarl[0]:
                eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
                print(eenheid, "°C", " => ", eenheid + 273.15, "K", sep="")
            else:
                if "f" in naarl[0]:
                    eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
                    print(eenheid, "°C", " => ", eenheid*9/5 + 32, "°F", sep="")
                else:
                    print("Deze eenheid bestaat niet!")
    else:
        if "k" in vanl[0]:
            naar = input("Naar welke eenheid wil je omzetten? ")
            naarl = naar.lower()
            if "c" in naarl[0]:
                eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
                print(eenheid, "K", " => ", eenheid - 273.15, "°C", sep="")
            else:
                if "k" in naarl[0]:
                    eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
                    print(eenheid, "K", " => ", eenheid, "K", sep="")
                else:
                    if "f" in naarl[0]:
                        eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
                        print(eenheid, "K", " => ", (eenheid - 273.15) * 9/5 + 32, "°F", sep="")
                    else:
                        print("Deze eenheid bestaat niet!")
        else:
            if "f" in vanl[0]:
                naar = input("Naar welke eenheid wil je omzetten? ")
                naarl = naar.lower()
                if "c" in naarl[0]:
                    eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER):"))
                    print(eenheid, "°F", " => ", (eenheid - 32)*5/9, "°C", sep="")
                else:
                    if "k" in naarl[0]:
                        eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
                        print(eenheid, "°F", " => ",(eenheid-32) * 5/9+273.15 , "K", sep="")
                    else:
                        if "f" in naarl[0]:
                            eenheid = float(input("Geef je temperatuur in (ENKEL HET CIJFER): "))
                            print(eenheid, "°F", " => ", eenheid , "°F", sep="")
                        else:
                            print("Deze eenheid bestaat niet!")
            else:
                print("Deze eenheid bestaat niet!")
    enter = input("Klik enter om nog te berekenen. Klik Ctrl+C om af te sluiten.")
    if enter == "":
        testl == ("")
