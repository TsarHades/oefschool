import matplotlib.pyplot as plt
import numpy

x = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
badschuim = numpy.array([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])
handzeep = numpy.array([9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 9999, 9200, 14400])
shampoo = numpy.array([1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800])
tandpasta = numpy.array([5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400])
scheerschuim = numpy.array([490, 280, 390, 1160, 1940, 1555, 1120, 2000, 1780, 1890, 1888, 2090])

plt.plot(x,badschuim,"-o")
plt.plot(x,handzeep,"-o")
plt.plot(x,shampoo,"-o")
plt.plot(x,tandpasta,"-o")
plt.plot(x,scheerschuim,"-o")

plt.show()
