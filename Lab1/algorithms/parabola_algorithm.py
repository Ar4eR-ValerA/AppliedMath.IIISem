def find_min(function, left_bound, right_bound, eps):
    segments = []
    calls = 0
    middle = (right_bound + left_bound) / 2

    left_result = function(left_bound)
    middle_result = function(middle)
    right_result = function(right_bound)
    calls += 3

    while abs(right_bound - left_bound) > eps:
        segments.append((left_bound, right_bound))

        if left_result < middle_result:
            right_bound = middle
            middle = (left_bound - right_bound) / 2

            right_result = middle_result
            middle_result = function(middle)
            calls += 1
        elif right_result < middle_result:
            left_bound = middle
            middle = (left_bound - right_bound) / 2

            left_result = middle_result
            middle_result = function(middle)
            calls += 1
        else:
            break

    left_point = left_bound
    inner_point = middle
    right_point = right_bound

    inner_result = middle_result

    while inner_point - left_point > eps and right_point - inner_point > eps:

        a1 = (inner_result - left_result) / (inner_point - left_point)
        a2 = 1 / (right_point - inner_point) * ((right_result - left_result) / (right_point - left_point) -
                                                (inner_result - left_result) / (inner_point - left_point))

        min_point = 1.0 / 2.0 * (left_point + inner_point - a1 / a2)

        if left_point < min_point < inner_point:
            right_point = inner_point
            inner_point = min_point

            right_result = inner_result
            inner_result = function(inner_point)
            calls += 1

            segments.append((inner_point, right_point))

        elif inner_point < min_point < right_point:
            left_point = inner_point
            inner_point = min_point

            left_result = inner_result
            inner_result = function(inner_point)
            calls += 1

            segments.append((left_point, inner_point))

        else:
            return inner_point, calls, segments

    return inner_point, calls, segments
