from math import sqrt, pow


def get_fibonacci_number(n):
    return -1 / sqrt(5) * pow((1 - sqrt(5)) / 2, n) + 1 / sqrt(5) * pow((1 + sqrt(5)) / 2, n)


def find_min(function, left_bound, right_bound, eps):
    segments = []
    calls = 0

    iteration_number = 1
    fibonacci_number_n = 1
    while fibonacci_number_n <= (right_bound - left_bound) / eps:
        iteration_number += 1
        fibonacci_number_n = get_fibonacci_number(iteration_number)

    prev_1 = get_fibonacci_number(iteration_number - 1)
    prev_2 = fibonacci_number_n - prev_1

    left_point = left_bound + (right_bound - left_bound) * prev_2 / fibonacci_number_n
    right_point = left_bound + (right_bound - left_bound) * prev_1 / fibonacci_number_n

    left_result = function(left_point)
    right_result = function(right_point)
    calls += 2

    for _ in range(iteration_number, 1, -1):
        segments.append((min(left_bound, right_bound), max(left_bound, right_bound)))

        if abs(right_bound - left_bound) < eps:
            return (segments[-1][0] + segments[-1][1]) / 2, calls, segments

        if left_result < right_result:
            right_bound = right_point

            right_point = left_point
            right_result = left_result

            left_point = left_bound + (right_bound - right_point)
            left_result = function(left_point)
            calls += 1
        else:
            left_bound = left_point

            left_point = right_point
            left_result = right_result

            right_point = right_bound + (left_bound - left_point)
            right_result = function(right_point)
            calls += 1

    return (segments[-1][0] + segments[-1][1]) / 2, calls, segments
