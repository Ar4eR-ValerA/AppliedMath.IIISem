import numpy as np
from tools.luDecomposition import lu_decomposition

n = 5
a = np.array([[10., -3., 5.], [-7., 6., -1.], [0., 2., 5.]])

output = lu_decomposition(a)

print("U:")
print(output[0])

print("L:")
print(output[1])
