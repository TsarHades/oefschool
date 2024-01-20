# importeer packages (voor PIL: installeer Pillow)
import numpy as np
from PIL import Image


# open afbeelding met opgegeven bestandsnaam en retourneer 3 Numpy-arrays met RGB-waardes
def open(bestandsnaam):
    invoer_afbeelding = Image.open(bestandsnaam)

    # splits de afbeelding op in RGB-waardes
    r_afbeelding_in, g_afbeelding_in, b_afbeelding_in = invoer_afbeelding.split()

    # converteer RGB-waardes naar Numpy-arrays
    r_in = np.uint32(np.array(r_afbeelding_in))
    g_in = np.uint32(np.array(g_afbeelding_in))
    b_in = np.uint32(np.array(b_afbeelding_in))

    return r_in, g_in, b_in


# creëer afbeelding vanuit Numpy-arrays
def maak_afbeelding(r_in, g_in, b_in):
    # converteer de 3 Numpy-arrays terug naar een afbeelding
    r_afbeelding_uit = Image.fromarray(np.uint8(r_in))
    g_afbeelding_uit = Image.fromarray(np.uint8(g_in))
    b_afbeelding_uit = Image.fromarray(np.uint8(b_in))
    uitvoer_afbeelding = Image.merge("RGB", (r_afbeelding_uit, g_afbeelding_uit, b_afbeelding_uit))

    return uitvoer_afbeelding


#########
# optie 0
#########
def geen_bewerking(r_in, g_in, b_in):
    # intialiseer de uitvoer matrices met dezelfde grootte
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))

    # kopieer waardes uit r_in, g_in en b_in naar r_uit, g_uit en b_uit
    for i in range(r_in.shape[0]):  # per rij
        for j in range(r_in.shape[1]):  # per kolom
            r_uit[i][j] = r_in[i][j]  # effect op rood
            g_uit[i][j] = g_in[i][j]  # effect op groen
            b_uit[i][j] = b_in[i][j]  # effect op blauw

    return r_uit, g_uit, b_uit


#########
# optie 1
#########
def filter(kleur, r_in, g_in, b_in):
    # intialiseer de uitvoer matrices met dezelfde grootte
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))

    for i in range(r_in.shape[0]):
        for j in range(r_in.shape[1]):
            if kleur == "g":
                r_uit[i][j] = r_in[i][j]
                g_uit[i][j] = 0
                b_uit[i][j] = b_in[i][j]
            if kleur == "r":
                r_uit[i][j] = 0
                g_uit[i][j] = g_in[i][j]
                b_uit[i][j] = b_in[i][j]
            if kleur == "b":
                r_uit[i][j] = r_in[i][j]
                g_uit[i][j] = g_in[i][j]
                b_uit[i][j] = 0
    return r_uit, g_uit, b_uit


#########
# optie 2
#########
def inverteer(r_in, g_in, b_in):
    # intialiseer de uitvoer matrices met dezelfde grootte
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))

    for i in range(r_in.shape[0]):
        for j in range(r_in.shape[1]):
            r_uit[i][j] = 255-r_in[i][j]
            g_uit[i][j] = 255-g_in[i][j]
            b_uit[i][j] = 255-b_in[i][j]

    return r_uit, g_uit, b_uit


#########
# optie 3
#########
def zwartwit(r_in, g_in, b_in):
    # intialiseer de uitvoer matrices met dezelfde grootte
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))
    for i in range(r_in.shape[0]):
        for j in range(r_in.shape[1]):
            if r_in[i][j]+b_in[i][j]+g_in[i][j]<=765/3:
                r_uit[i][j] = 0
                g_uit[i][j] = 0
                b_uit[i][j] = 0
            else:
                r_uit[i][j] = 255
                g_uit[i][j] = 255
                b_uit[i][j] = 255
    return r_uit, g_uit, b_uit


#########
# optie 4
#########
def grijswaarde(r_in, g_in, b_in):
    # intialiseer de uitvoer matrices met dezelfde grootte
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))

    for i in range(r_in.shape[0]):
        for j in range(r_in.shape[1]):
            r_uit[i][j] = (r_in[i][j]+g_in[i][j]+b_in[i][j])/3
            g_uit[i][j] = (r_in[i][j]+g_in[i][j]+b_in[i][j])/3
            b_uit[i][j] = (r_in[i][j]+g_in[i][j]+b_in[i][j])/3

    return r_uit, g_uit, b_uit


#########
# optie 5
#########
def verduister_verhelder(modus, r_in, g_in, b_in):
    # intialiseer de uitvoer matrices met dezelfde grootte
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))
    for i in range(r_in.shape[0]):
        for j in range(r_in.shape[1]):
            if modus == "d":
                r_uit[i][j] = r_in[i][j]*0.7
                g_uit[i][j] = g_in[i][j]*0.7
                b_uit[i][j] = b_in[i][j]*0.7
            else:
                r_uit[i][j] = r_in[i][j] * 1.3
                g_uit[i][j] = g_in[i][j] * 1.3
                b_uit[i][j] = b_in[i][j] * 1.3
                if b_uit[i][j]>255:
                    b_uit[i][j]=255
                if g_uit[i][j] > 255:
                    g_uit[i][j] = 255
                if r_uit[i][j] > 255:
                    r_uit[i][j] = 255
    return r_uit, g_uit, b_uit


#########
# optie 6
#########
def spiegel(modus, r_in, g_in, b_in):
    # intialiseer de uitvoer matrices met dezelfde grootte
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))

    for i in range(r_in.shape[0]):
        for j in range(r_in.shape[1]):
            if modus == "v":
                r_uit[i][j] = r_in[i][-j]
                g_uit[i][j] = g_in[i][-j]
                b_uit[i][j] = b_in[i][-j]
            else:
                r_uit[i][j] = r_in[-i][j]
                g_uit[i][j] = g_in[-i][j]
                b_uit[i][j] = b_in[-i][j]

    return r_uit, g_uit, b_uit


#########
# optie 7
#########
def roteer(modus, r_in, g_in, b_in):
    # TODO: intialiseer de uitvoer matrices waarbij breedte en hoogte omgewisseld zijn
    r_uit = np.zeros((r_in.shape[0], r_in.shape[1]))
    g_uit = np.zeros((g_in.shape[0], g_in.shape[1]))
    b_uit = np.zeros((b_in.shape[0], b_in.shape[1]))

    # TODO: roteer afbeelding 90 graden wijzerzin of tegenwijzerzin volgens opgegeven modus ("w", "t")
    for i in range(r_in.shape[0]):
        for j in range(r_in.shape[1]):
            r_uit[i][j] = r_in[i][j]
            g_uit[i][j] = g_in[i][j]
            b_uit[i][j] = b_in[i][j]

    return r_uit, g_uit, b_uit


def main():
    r_in, g_in, b_in = open("landschap1.jpg")

    doorgaan = "j"
    while (doorgaan == "j"):
        optie = int(input("Geef optie in (0 - 11): "))

        if optie == 0:
            print("> Geen bewerkingen op de afbeelding")
            r_uit, g_uit, b_uit = geen_bewerking(r_in, g_in, b_in)

        elif optie == 1:
            print("> Kleur wegfilteren van afbeelding")
            kleur = input("  Geef kleur in (r, g of b): ")
            r_uit, g_uit, b_uit = filter(kleur, r_in, g_in, b_in)

        elif optie == 2:
            print("> Afbeelding inverteren")
            r_uit, g_uit, b_uit = inverteer(r_in, g_in, b_in)

        elif optie == 3:
            print("> Afbeelding zwart-wit maken")
            r_uit, g_uit, b_uit = zwartwit(r_in, g_in, b_in)

        elif optie == 4:
            print("> Afbeelding in grijswaarden weergeven")
            r_uit, g_uit, b_uit = grijswaarde(r_in, g_in, b_in)

        elif optie == 5:
            print("> Afbeelding verduisteren of verhelderen")
            modus = input("  Geef modus in (d: verduisteren, h: verhelderen): ")
            r_uit, g_uit, b_uit = verduister_verhelder(modus, r_in, g_in, b_in)

        elif optie == 6:
            print("> Afbeelding horizontaal of verticaal spiegelen")
            modus = input("  Geef modus in (h: horizontaal, v: verticaal): ")
            r_uit, g_uit, b_uit = spiegel(modus, r_in, g_in, b_in)

        elif optie == 7:
            print("> Afbeelding 90 graden wijzerzin of tegenwijzerzin roteren")
            modus = input("  Geef modus in (w: wijzerzin, t: tegenwijzerzin): ")
            r_uit, g_uit, b_uit = roteer(modus, r_in, g_in, b_in)

        else:  # standaard geen bewerking
            r_uit, g_uit, b_uit = geen_bewerking(r_in, g_in, b_in)

        uitvoer_afbeelding = maak_afbeelding(r_uit, g_uit, b_uit)
        uitvoer_afbeelding.show()

        doorgaan = input("Doorgaan met volgende bewerking (j/n)? ")


main()