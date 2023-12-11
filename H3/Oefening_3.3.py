import matplotlib.pyplot as plt
import numpy
interval = numpy.arange(0,2*numpy.pi,0.01)
x = numpy.sin(interval)
y = numpy.sin(interval)
plt.plot(x,y)
plt.show()

x = numpy.cos(interval)
y = numpy.sin(interval)
plt.plot(x,y)
plt.show()

x = numpy.sin(2*interval)
y = numpy.sin(interval)
plt.plot(x,y)
plt.show()

x = numpy.cos(3*interval)
y = numpy.sin(interval)
plt.plot(x,y)
plt.show()

