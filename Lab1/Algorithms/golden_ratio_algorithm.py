from math import sqrt


def find_min(function, left_bound, right_bound, eps):
    golden_ratio = (sqrt(5) + 1) / 2
    segments = []

    while right_bound - left_bound > eps:
        segments.append((left_bound, right_bound))

        left_point = right_bound - (right_bound - left_bound) / golden_ratio
        right_point = left_bound + (right_bound - left_bound) / golden_ratio

        left_result = function(left_point)
        right_result = function(right_point)

        if left_result < right_result:
            right_bound = right_point
        else:
            left_bound = left_point

    segments.append((right_bound + left_bound) / 2)
    return segments[-1], segments
