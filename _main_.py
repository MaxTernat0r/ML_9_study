from random import randint
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import csv

X = []
Y = []
with open("datasets/dataset.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=';')
    for row in file_reader:
        X.append(row[0])
        Y.append(row[1])

X = [[x] for x in X]
Y = [[y] for y in Y]

print(X)
print(Y)

# # Возьмем значения X от 5 до 60 и для каждого посчитаем Y по формул kx + b
# X = [i for i in range(5, 60)]
# Y = [1.2 * x + 44 + randint(-20, 20) for x in X]
# # Для библиотеки matplotlib потребуется перевести все X в двумерный массив, где у каждого вложенного списка один элемент
# X = [[x] for x in X]
# Y = [[y] for y in Y]
# # print(X[:10])
# # print(Y[:10])
#
# # Теперь возьмем готовую модель линейной регрессии
# regressor = LinearRegression()
# regressor.fit(X, Y)

# print("k = ", regressor.coef_)
# print("b = ", regressor.intercept_)
#
# plt.plot(X, Y, 'o')
# plt.show()
#
# # На основе этой модели посчитаем неизвестные коэффиценты и предположим Y
# k = regressor.coef_
# b = regressor.intercept_
# predicted_Y = regressor.predict(X)
#
# # Выводим график
# plt.plot(X, Y, 'o')
# plt.plot(X, predicted_Y)
# plt.show()
#
# # Считаем среднюю ошибку
# print('Средняя ошибка предсказания:', metrics.mean_squared_error(Y, predicted_Y) ** 0.5)
