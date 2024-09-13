import numpy
import matplotlib.pyplot as plt

#сгенерируем случайных чисел с помощью numpy
data = numpy.random.normal(100, 50, 1000)

#теперь отрисуем гистограмму
plt.hist(data)
plt.show()

#вычислим среднее значение
print(sum(data) / len(data))

#вычислим стандартное отклонение
N = len(data)
mean = sum(data) / N

S = 0
for x in data:
    S += (x - mean) ** 2

std = (S / (N - 1)) ** 0.5

print("стандартное отклонение: ", std)

