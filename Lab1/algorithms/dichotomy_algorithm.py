def find_min(function, left_bound, right_bound, eps):
    segments = []

    while right_bound - left_bound > eps:
        segments.append((left_bound, right_bound))

        middle = (left_bound + right_bound) / 2

        left_result = function(middle - eps)
        right_result = function(middle + eps)

        if left_result < right_result:
            right_bound = middle
        else:
            left_bound = middle

    segments.append((left_bound, right_bound))
    return (left_bound + right_bound) / 2, segments
