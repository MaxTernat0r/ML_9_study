import numpy
import matplotlib.pyplot as plt

data = numpy.random.normal(100, 50, 1000)
plt.hist(data)
print(sum(data) / len(data))
plt.show()

N = len(data)
mean = sum(data) / N

S = 0
for x in data:
    S += (x - mean) ** 2

std = (S / (N - 1)) ** 0.5

print("стандартное отклонение: ", std)