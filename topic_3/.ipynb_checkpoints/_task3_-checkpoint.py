import numpy as np
data = np.array(range(1, 1000))
print(data[((data % 3 == 0) | (data % 5 == 0)) & (data % 15 != 0)])
