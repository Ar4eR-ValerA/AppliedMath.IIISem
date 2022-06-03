from tools import matrix_generator
from tools import jacobi_method
import numpy as np


A = np.array([[17, -2, -2], [-2, 14, -4], [-2, -4, 14]])
print("Матрица 1:")
print(A)
ans, vec, iters = jacobi_method.jacobi_solve(A, 0.1)
print("\nСобственные числа:")
print(ans)
print("\nСобственные векторы:")
print(vec)
print("\nКол-во итераций:")
print(iters)


print("______________________________________\n")
B = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]])
print("Матрица 2:")
print(B)
ans, vec, iters = jacobi_method.jacobi_solve(B, 0.1)
print("\nСобственные числа:")
print(ans)
print("\nСобственные векторы:")
print(vec)
print("\nКол-во итераций:")
print(iters)