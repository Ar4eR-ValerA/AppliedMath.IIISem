import math
from algorithms import dichotomy_algorithm, golden_ratio_algorithm, \
    fibonacci_algorithm, parabola_algorithm, brent_algorithm


def our_function(x):
    return math.sin(x) * math.pow(x, 3)


def unimodal_function(x):
    return math.log(1 / x, 10) + pow(x, 0.7)


# print("Our function:")
#
# print("Dichotomy algorithm:")
# ans, calls, segments = dichotomy_algorithm.find_min(our_function, 3, 6, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("GoldenRatio algorithm:")
# ans, calls, segments = golden_ratio_algorithm.find_min(our_function, 3, 6, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("Fibonacci algorithm:")
# ans, calls, segments = fibonacci_algorithm.find_min(our_function, 3, 6, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("Parabola algorithm:")
# ans, calls, segments = parabola_algorithm.find_min(our_function, 3, 6, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("Brent algorithm:")
# ans, calls, segments = brent_algorithm.find_min(our_function, 3, 6, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
#
# print("Unimodal function:")
#
# print("Dichotomy algorithm:")
# ans, calls, segments = dichotomy_algorithm.find_min(unimodal_function, 0.1, 2, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("GoldenRatio algorithm:")
# ans, calls, segments = golden_ratio_algorithm.find_min(unimodal_function, 0.1, 2, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("Fibonacci algorithm:")
# ans, calls, segments = fibonacci_algorithm.find_min(unimodal_function, 0.1, 2, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("Parabola algorithm:")
# ans, calls, segments = parabola_algorithm.find_min(unimodal_function, 0.1, 2, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")
#
# print("Brent algorithm:")
# ans, calls, segments = brent_algorithm.find_min(unimodal_function, 0.1, 2, 1e-8)
# print(calls, len(segments), ans)
# print(segments, "\n")


print("Dichotomy algorithm:")
ans, calls, segments = dichotomy_algorithm.find_min(our_function, 3, 6, 1e-4)
print(ans)

print("GoldenRatio algorithm:")
ans, calls, segments = golden_ratio_algorithm.find_min(our_function, -15, -3, 1e-4)
print(ans)

print("Fibonacci algorithm:")
ans, calls, segments = fibonacci_algorithm.find_min(our_function, -15, -3, 1e-4)
print(ans)

print("Parabola algorithm:")
ans, calls, segments = parabola_algorithm.find_min(our_function, -15, -3, 1e-4)
print(ans)

print("Brent algorithm:")
ans, calls, segments = brent_algorithm.find_min(our_function, -15, -3, 1e-4)
print(ans)
