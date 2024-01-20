# importeer packages (voor PIL: installeer Pillow)
import numpy as np
from PIL import Image


# open afbeelding met opgegeven bestandsnaam en retourneer 3 Numpy-arrays met RGB-waardes
def open(bestandsnaam):
    invoer_afbeelding = Image.open(bestandsnaam)

    # converteer afbeelding naar 3D Numpy-array
    afbeelding_in = np.uint32(np.array(invoer_afbeelding))

    return afbeelding_in


# creëer afbeelding vanuit Numpy-arrays
def maak_afbeelding(afbeelding_in):
    # converteer de 3D Numpy-array terug naar een afbeelding
    afbeelding_uit = Image.fromarray(np.uint8(afbeelding_in))

    return afbeelding_uit


#########
# optie 0
#########
def geen_bewerking(afbeelding_in):
    # intialiseer de 3D uitvoer matrix met dezelfde grootte
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    # kopieer waardes uit afbeelding_in naar afbeelding_uit
    for i in range(afbeelding_in.shape[0]):  # per rij
        for j in range(afbeelding_in.shape[1]):  # per kolom
            afbeelding_uit[i][j] = afbeelding_in[i][j]

    return afbeelding_uit


#########
# optie 1
#########
def filter(kleur, afbeelding_in):
    # intialiseer de 3D uitvoer matrix met dezelfde grootte
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    # TODO: filter de opgegeven kleur ("r", "g", "b") uit
    for i in range(afbeelding_in.shape[0]):
        for j in range(afbeelding_in.shape[1]):
            afbeelding_uit[i][j][0] = afbeelding_in[i][j][0]
            afbeelding_uit[i][j][1] = afbeelding_in[i][j][1]
            afbeelding_uit[i][j][2] = afbeelding_in[i][j][2]

    return afbeelding_uit


#########
# optie 2
#########
def inverteer(afbeelding_in):
    # intialiseer de 3D uitvoer matrix met dezelfde grootte
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    # TODO: inverteer elke kleur naar zijn tegengestelde
    for i in range(afbeelding_in.shape[0]):
        for j in range(afbeelding_in.shape[1]):
            afbeelding_uit[i][j][0] = afbeelding_in[i][j][0]
            afbeelding_uit[i][j][1] = afbeelding_in[i][j][1]
            afbeelding_uit[i][j][2] = afbeelding_in[i][j][2]

    return afbeelding_uit


#########
# optie 3
#########
def zwartwit(afbeelding_in):
    # intialiseer de 3D uitvoer matrix met dezelfde grootte
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    # TODO: maak van de afbeelding zwart-witwaarden
    for i in range(afbeelding_in.shape[0]):
        for j in range(afbeelding_in.shape[1]):
            afbeelding_uit[i][j][0] = afbeelding_in[i][j][0]
            afbeelding_uit[i][j][1] = afbeelding_in[i][j][1]
            afbeelding_uit[i][j][2] = afbeelding_in[i][j][2]

    return afbeelding_uit


#########
# optie 4
#########
def grijswaarde(afbeelding_in):
    # intialiseer de 3D uitvoer matrix met dezelfde grootte
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    # TODO: maak van de afbeelding grijswaarden
    for i in range(afbeelding_in.shape[0]):
        for j in range(afbeelding_in.shape[1]):
            afbeelding_uit[i][j][0] = afbeelding_in[i][j][0]
            afbeelding_uit[i][j][1] = afbeelding_in[i][j][1]
            afbeelding_uit[i][j][2] = afbeelding_in[i][j][2]

    return afbeelding_uit


#########
# optie 5
#########
def verduister_verhelder(modus, afbeelding_in):
    # intialiseer de 3D uitvoer matrix met dezelfde grootte
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    factor_donker = 0.5
    factor_helder = 1.4

    # TODO: verduister of verhelder afbeelding volgens opgegeven modus ("d", "h")
    for i in range(afbeelding_in.shape[0]):
        for j in range(afbeelding_in.shape[1]):
            afbeelding_uit[i][j][0] = afbeelding_in[i][j][0]
            afbeelding_uit[i][j][1] = afbeelding_in[i][j][1]
            afbeelding_uit[i][j][2] = afbeelding_in[i][j][2]

    return afbeelding_uit


#########
# optie 6
#########
def spiegel(modus, afbeelding_in):
    # intialiseer de 3D uitvoer matrix met dezelfde grootte
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    # TODO: spiegel afbeelding horizontaal of verticaal volgens opgegeven modus ("h", "v")
    for i in range(afbeelding_in.shape[0]):
        for j in range(afbeelding_in.shape[1]):
            afbeelding_uit[i][j][0] = afbeelding_in[i][j][0]
            afbeelding_uit[i][j][1] = afbeelding_in[i][j][1]
            afbeelding_uit[i][j][2] = afbeelding_in[i][j][2]

    return afbeelding_uit


#########
# optie 7
#########
def roteer(modus, afbeelding_in):
    # TODO: intialiseer de 3D uitvoer matrix waarbij breedte en hoogte omgewisseld zijn
    afbeelding_uit = np.zeros((afbeelding_in.shape[0], afbeelding_in.shape[1], 3))

    # TODO: roteer afbeelding 90 graden wijzerzin of tegenwijzerzin volgens opgegeven modus ("w", "t")
    for i in range(afbeelding_in.shape[0]):
        for j in range(afbeelding_in.shape[1]):
            afbeelding_uit[i][j][0] = afbeelding_in[i][j][0]
            afbeelding_uit[i][j][1] = afbeelding_in[i][j][1]
            afbeelding_uit[i][j][2] = afbeelding_in[i][j][2]

    return afbeelding_uit


def main():
    afbeelding_in = open("landschap1.jpg")

    doorgaan = "j"
    while (doorgaan == "j"):
        optie = int(input("Geef optie in (0 - 11): "))

        if optie == 0:
            print("> Geen bewerkingen op de afbeelding")
            afbeelding_uit = geen_bewerking(afbeelding_in)

        elif optie == 1:
            print("> Kleur wegfilteren van afbeelding")
            kleur = input("  Geef kleur in (r, g of b): ")
            afbeelding_uit = filter(kleur, afbeelding_in)

        elif optie == 2:
            print("> Afbeelding inverteren")
            afbeelding_uit = inverteer(afbeelding_in)

        elif optie == 3:
            print("> Afbeelding zwart-wit maken")
            afbeelding_uit = zwartwit(afbeelding_in)

        elif optie == 4:
            print("> Afbeelding in grijswaarden weergeven")
            afbeelding_uit = grijswaarde(afbeelding_in)

        elif optie == 5:
            print("> Afbeelding verduisteren of verhelderen")
            modus = input("  Geef modus in (d: verduisteren, h: verhelderen): ")
            afbeelding_uit = verduister_verhelder(modus, afbeelding_in)

        elif optie == 6:
            print("> Afbeelding horizontaal of verticaal spiegelen")
            modus = input("  Geef modus in (h: horizontaal, v: verticaal): ")
            afbeelding_uit = spiegel(modus, afbeelding_in)

        elif optie == 7:
            print("> Afbeelding 90 graden wijzerzin of tegenwijzerzin roteren")
            modus = input("  Geef modus in (w: wijzerzin, t: tegenwijzerzin): ")
            afbeelding_uit = roteer(modus, afbeelding_in)

        else:  # standaard geen bewerking
            afbeelding_uit = geen_bewerking(afbeelding_in)

        uitvoer_afbeelding = maak_afbeelding(afbeelding_uit)
        uitvoer_afbeelding.show()

        doorgaan = input("Doorgaan met volgende bewerking (j/n)? ")


main()