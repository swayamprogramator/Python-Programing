import numpy as np
num = np.array([[5, 7, 8]])
new = np.append(num, [[4, 5, 6], [4, 9, 0], [2, 3, 1]], axis=0)
print(new)