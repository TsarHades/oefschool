import matplotlib.pyplot as plt
import numpy
interval = numpy.arange(-5,5,0.01)
cosstuff = numpy.cos(interval)
plt.plot(interval,cosstuff,"-.r")
plt.xlabel("Invoer")
plt.ylabel("Functiewaarden")
plt.title("De cosinus-functie")
plt.show()