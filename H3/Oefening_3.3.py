import matplotlib.pyplot as plt
import numpy

##deel a
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

##deel b
xtemp = 16*(numpy.sin(interval))
x = numpy.power(xtemp, 3)
y = 13*(numpy.cos(interval))-5*(numpy.cos(2*interval)) - 2*numpy.cos(3*interval) - numpy.cos(4*interval)
plt.plot(x,y)
plt.show()
