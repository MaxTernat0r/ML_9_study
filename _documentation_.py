from random import randint
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Сгенерируем несколько значений X и для каждого значения Y по формуле y = kx + b:
X = [i for i in range(5, 60)]
Y = [1.2 * x + 44 + randint(-20, 20) for x in X]

# Библиотека для машинного обучения sklearn требует чтобы коэффиценты X лежали каждый в отдельном массиве в двумерном массиве. Переведем:
X = [[x] for x in X]

# Создадим объект нужного класса, после передадим в него значения:
regressor = LinearRegression()
regressor.fit(X, Y)

# Рассчитаем с помощью библиотеки коэффиценты k и b для линейной функции:
k = regressor.coef_
b = regressor.intercept_
predicted_Y = regressor.predict(X)

# Построим график функции:
plt.plot(X, Y, 'o')
plt.plot(X, predicted_Y)
plt.show()

# Выведем коэффиценты k и b:
print(*k, b)

# Найдем насколько график неточен:
print('Средняя ошибка предсказания:', metrics.mean_squared_error(Y, predicted_Y) ** 0.5)
