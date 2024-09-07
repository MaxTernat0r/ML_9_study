from sklearn.linear_model import LinearRegression
import csv

X = []
Y = []
with open("datasets/dataset.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=';')
    for row in file_reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))

X = [[x] for x in X]
print(X)
regressor = LinearRegression()
regressor.fit(X, Y)

print("k =", *regressor.coef_)
print("b =", regressor.intercept_)
