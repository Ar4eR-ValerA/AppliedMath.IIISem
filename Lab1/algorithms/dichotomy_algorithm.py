def find_min(function, left_bound, right_bound, eps):
    segments = []
    calls = 0

    while right_bound - left_bound > eps:
        segments.append((left_bound, right_bound))

        middle = (left_bound + right_bound) / 2

        delta = eps / 2 * 0.9
        left_result = function(middle - delta)
        right_result = function(middle + delta)
        calls += 2

        if left_result < right_result:
            right_bound = middle + delta
        else:
            left_bound = middle - delta

    segments.append((left_bound, right_bound))
    return (left_bound + right_bound) / 2, calls, segments
