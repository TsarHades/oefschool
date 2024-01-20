import matplotlib.pyplot as plt
import numpy as np
def teken_subplot():
    teller = 0
    plotnumber = 321
    while teller != 6:
        plt.subplot(plotnumber)
        puntenx2 = np.random.randn((teller + 1) * 10)
        punteny2 = np.random.randn((teller + 1) * 10)
        plt.scatter(puntenx2, punteny2)
        teller += 1
        plotnumber += 1

puntenx  = np.random.randn(10)
punteny = np.random.randn(10)
plt.scatter(puntenx, punteny)
plt.show()

teken_subplot()
plt.suptitle("Genereren van punten (van n = 10 t.e.m. n = 60)")
plt.show()