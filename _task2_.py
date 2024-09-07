from sklearn.linear_model import LinearRegression
import csv

X = []
Y = []
with open("datasets/boston.csv", encoding='utf-8') as r_file:
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


print("k =", *regressor.coef_)
print("b =", regressor.intercept_)

