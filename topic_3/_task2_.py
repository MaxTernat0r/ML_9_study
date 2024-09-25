import numpy as np
data = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
X = np.array(data)
print(np.sum(X), np.mean(X))
print(X.mean(axis=0), X.std(axis=0))
