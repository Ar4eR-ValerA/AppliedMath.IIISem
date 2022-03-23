import math
from Algorithms import dichotomy_algorithm, golden_ratio_algorithm, \
    fibonacci_algorithm, parabola_algorithm, brent_algorithm


#def function(x):
#    return math.sin(x) * math.pow(x, 3)

def function(x):
    return math.sin(x) * math.pow(x, 3)


print("Dichotomy algorithm:")
ans, segments = dichotomy_algorithm.find_min(function, 3, 6, 1e-8)
print(len(segments), ans)
print(segments, "\n")

print("GoldenRatio algorithm:")
ans, segments = golden_ratio_algorithm.find_min(function, 3, 6, 1e-8)
print(len(segments), ans)
print(segments, "\n")

print("Fibonacci algorithm:")
ans, segments = fibonacci_algorithm.find_min(function, 3, 6, 1e-8)
print(len(segments), ans)
print(segments, "\n")

print("Parabola algorithm:")
ans, segments = parabola_algorithm.find_min(function, 3, 6, 1e-8)
print(len(segments), ans)
print(segments, "\n")

print("Brent algorithm:")
ans, segments = brent_algorithm.find_min(function, 3, 6, 1e-8)
print(len(segments), ans)
print(segments, "\n")
