# Для начала надо понять что такое вообще линейная регрессия. Об этом написано тут -> https://codingprojects.ru/insider/courses/145/steps/2314
# Как мы поняли функция линейной регрессии создается стандартным образом: Y = k * X + b. То есть, зная Y и X всех точек нейронная сеть сможет рассчитать k и b.
# К счастью, у нас как раз есть файл data.csv, который дается в задании. Он имеет следующий вид: X;Y
#                                                                                                X;Y и так далее
# Короче, много-много строк где сначала написан X, потом точка с запятой как разделитель и Y. Этот файл называется датасет.
# Нам остается только передать в нейронку этот датасет, обучить ее на ее основе и на полученных данных она сама рассчитает k и b для линейной регрессии, которые мы и ищем.


# Подключение библиотек. sklearn нужна для обучения, csv для работы с датасетом
from sklearn.linear_model import LinearRegression
import csv

# Создаем два массива, в первый мы будем класть все X, в другой все Y.
X = []
Y = []

# Открываем файл. По правилам Python для работы с файлом его нужно сначала открыть с каким-то параметром (write или read) и потом его закрыть.
# Но можно использовать в начале with - это гарантирует что после работы с файлом он будет закрыт. r_file - параметр read для чтения файла, но не изменения его.
with open("datasets/dataset.csv", encoding='utf-8') as r_file:
    # В массив file_reader запишем датасет с разделителем ";", то есть теперь он понимает что есть X, а что есть Y, и какой X к какому Y принадлежит.
    file_reader = csv.reader(r_file, delimiter=';')
    # Пройдемся по всему массиву, все X запишем как числа с плавающей точкой в массив X, все Y как числа с плавающей точкой в массив Y.
    for row in file_reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))

# Сейчас мы работаем с одномерной регрессией. Однако регрессия бывает еще и многомерная (-> https://codingprojects.ru/insider/courses/145/steps/2316), поэтому
# sklearn требует чтобы массив X содержал не просто иксы, а вложенные массивы с X. То есть этим генератором мы переводим массив X из [1, 2, 3, 4] в [[1], [2], [3], [4]].
# Это нужно просто потому что так просит библиотека, иначе нейронка не обучится и будет ошибка.
X = [[x] for x in X]

# Создаем переменную "обученной нейронки". Назовем ее regressor. Обозначим, что учить мы ее будем линейной регрессии, вызвав функцию, чтобы она подготовилась.
regressor = LinearRegression()
# Обучим нейронку. Закинем в нее значения из X и из Y, которые мы так усердно готовили. Теперь она обучена и готова рассчитать нам наши значения.
regressor.fit(X, Y)

# Собственно говоря, функции .сoef_ и .intercept_ и рассчитывают k и b соответственно. Вызываем их в нашей переменной с обученной нейронкой.
# Звездочка перед regressor.coef_ нужна так как, напомню, X у нас в виде вложенных массивов, и звездочка убирает квадратные скобки вокруг числа.
print("k =", *regressor.coef_)
print("b =", regressor.intercept_)
