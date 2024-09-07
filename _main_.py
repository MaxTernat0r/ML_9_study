from random import randint
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [i for i in range(5, 60)]
Y = [1.2 * x + 44 + randint(-20, 20) for x in X]

X = [[x] for x in X]
# print(X[:10])
# print(Y[:10])

regressor = LinearRegression()
regressor.fit(X, Y)

# print("k = ", regressor.coef_)
# print("b = ", regressor.intercept_)
#
# plt.plot(X, Y, 'o')
# plt.show()

k = regressor.coef_
b = regressor.intercept_
predicted_Y = regressor.predict(X)

plt.plot(X, Y, 'o')
plt.plot(X, predicted_Y)
plt.show()
