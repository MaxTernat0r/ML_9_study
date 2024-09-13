import numpy
import matplotlib.pyplot as plt

data = numpy.random.normal(100, 50, 1000)
plt.hist(data)
plt.show()