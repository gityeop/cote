import numpy as np
from scipy.stats import mode

a = [2, 2, 3, 5, 5, 5, 8, 14, 22, 37, 62]

print(sum(a)/len(a))
print(np.median(a))
print(mode(a))