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

print("\nМатрица A * собственный вектор №1:", np.dot(A, vec.transpose()[0]))
print("Собственное число №1 * собственный вектор №1:", np.dot(ans[0], vec.transpose()[0]))

print("\nМатрица A * собственный вектор №2:", np.dot(A, vec.transpose()[1]))
print("Собственное число №2 * собственный вектор №2:", np.dot(ans[1], vec.transpose()[1]))

print("\nМатрица A * собственный вектор №3:", np.dot(A, vec.transpose()[2]))
print("Собственное число №3 * собственный вектор №3", np.dot(ans[2], vec.transpose()[2]))

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

print("\nМатрица B * собственный вектор №1:", np.dot(B, vec.transpose()[0]))
print("Собственное число №1 * собственный вектор №1:", np.dot(ans[0], vec.transpose()[0]))

print("\nМатрица B * собственный вектор №2:", np.dot(B, vec.transpose()[1]))
print("Собственное число №2 * собственный вектор №2:", np.dot(ans[1], vec.transpose()[1]))

print("\nМатрица B * собственный вектор №3:", np.dot(B, vec.transpose()[2]))
print("Собственное число №3 * собственный вектор №3:", np.dot(ans[2], vec.transpose()[2]))