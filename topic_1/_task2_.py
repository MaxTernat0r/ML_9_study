from sklearn.linear_model import LinearRegression
import csv
from sklearn import metrics

X = []
Y = []
total = 0
with open("../datasets/boston.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=',')
    cnt = 0
    for row in file_reader:
        if cnt != 0:
            X.append(tuple([float(i) for i in row[:13]]))
            Y.append(float(row[-1]))
        else:
            cnt = 1

regressor = LinearRegression()
regressor.fit(X, Y)
predicted_Y = regressor.predict(X)

print(f'Предположительная стоимость квартир (medv): {Y}')

for i in range(len(Y)):
    total += Y[i]
error = metrics.mean_squared_error(Y, predicted_Y) ** 0.5
print(
    f'Средняя ошибка предсказания равняется {metrics.mean_squared_error(Y, predicted_Y) ** 0.5}, что достаточно много, так как составляет примерно {error * 100 // (total / len(Y))}% от средней стоимости квартир.')
