def find_min(function, left_bound, right_bound, eps):
    segments = []
    calls = 0
    middle = (right_bound + left_bound) / 2

    while abs(right_bound - left_bound) > eps:
        segments.append((left_bound, right_bound))

        left_result = function(left_bound)
        middle_result = function(middle)
        right_result = function(right_bound)
        calls += 3

        if left_result < middle_result:
            right_bound = middle
        elif right_result < middle_result:
            left_bound = middle
        else:
            break

    left_point = left_bound
    inner_point = middle
    right_point = right_bound
    while inner_point - left_point > eps and right_point - inner_point > eps:

        left_result = function(left_point)
        inner_result = function(inner_point)
        right_result = function(right_point)
        calls += 3

        a1 = (inner_result - left_result) / (inner_point - left_point)
        a2 = 1 / (right_point - inner_point) * ((right_result - left_result) / (right_point - left_point) -
                                                (inner_result - left_result) / (inner_point - left_point))

        min_point = 1.0 / 2.0 * (left_point + inner_point - a1 / a2)

        if left_point < min_point < inner_point:
            right_point = inner_point
            inner_point = min_point
            segments.append((inner_point, right_point))

        elif inner_point < min_point < right_point:
            left_point = inner_point
            inner_point = min_point
            segments.append((left_point, inner_point))

        else:
            return inner_point, calls, segments

    return inner_point, calls, segments
