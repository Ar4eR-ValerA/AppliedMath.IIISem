from math import sqrt


def find_min(function, left_bound, right_bound, eps):
    golden_ratio = (sqrt(5) + 1) / 2
    segments = []
    calls = 0

    left_point = right_bound - (right_bound - left_bound) / golden_ratio
    right_point = left_bound + (right_bound - left_bound) / golden_ratio
    calls += 2

    left_result = function(left_point)
    right_result = function(right_point)

    while right_bound - left_bound > eps:
        segments.append((left_bound, right_bound))

        if left_result < right_result:
            right_bound = right_point
            right_result = left_result

            right_point = left_point
            left_point = right_bound - (right_bound - left_bound) / golden_ratio

            left_result = function(left_point)
            calls += 1

        else:
            left_bound = left_point
            left_result = right_result

            left_point = right_point
            right_point = left_bound + (right_bound - left_bound) / golden_ratio

            right_result = function(right_point)
            calls += 1


    segments.append((left_bound, right_bound))
    return (right_bound + left_bound) / 2, calls, segments
