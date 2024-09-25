from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Подгружаем датасет
X, Y = load_diabetes(return_X_y=True)
feature_names = ["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"]

# Обучаем модель
model = LinearRegression()
model.fit(X, Y)

# Предугадываем Y
Y_predicted = model.predict(X)

# Масштабируем данные
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

# Заново обучаем модель на уже масштабированных данных
model_scaled = LinearRegression()
model_scaled.fit(X_scaled, Y)

Y_predicted2 = model_scaled.predict(X_scaled)

print("Рассмотрим все коэффиценты датасета:")
for value, name in sorted(zip(model_scaled.coef_, feature_names), reverse=True):
    print(round(value, 2), "-", name)
print(
    "Получается, что s5 влияет сильнее всего в положительную сторону, s1 в отрицательную, а age практически не имеет влияния. Таким образом мы можем сделать вывод, что динамика развития сахарного диабета почти не зависит от возраста.")

# Посчитаем RMSE
mse = mean_squared_error(Y, Y_predicted)
print("RMSE = ", mse ** 0.5)

# Посчитаем стандартное отклонение
N = len(Y)
mean = sum(Y) / N
S = 0
for y in Y:
    S += (y - mean) ** 2

std = (S / (N - 1)) ** 0.5
print("Cтандартное отклонение: ", std)

# Средний % ошибки
S = [((y - y_predicted) / y) ** 2 for (y, y_predicted) in zip(Y, Y_predicted)]
relative_mse = (sum(S)/len(S))
print(f'Средний % ошибки {(relative_mse ** 0.5) * 100}, что очень много.')

# Построим регрессию
plt.plot(X, Y, 'o')
plt.plot(X, Y)
plt.show()
