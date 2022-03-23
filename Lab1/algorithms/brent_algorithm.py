from math import fabs, sqrt

const = (3 - sqrt(5)) / 2

def find_min(function, left_bound, right_bound, eps):

    def find_parabola_min(f, l, m, r):
        if l == m or m == r or l == r:
            return None

        left_res = f(l)
        right_res = f(r)
        middle_res = f(m)

        a1 = (middle_res - left_res) / (m - l)
        a2 = 1 / (r - m) * ((right_res - left_res) / (r - l) - (middle_res - left_res) / (m - l))

        if a2 == 0:
            return None

        return 1.0 / 2.0 * (l + m - a1 / a2)

    middle = (left_bound + right_bound) / 2.0
    left_point = right_point = middle
    middle_result = function(middle)
    left_result = right_result = middle_result
    prev_len = current_len = right_bound - left_bound
    segments = []
    calls = 1

    while fabs(right_bound - left_bound) >= 2 * eps:
        segments.append([min(left_bound, right_bound), max(left_bound, right_bound)])
        prev_prev_len = prev_len
        prev_len = current_len
        parabola_min = 0
        parabola_fl = False

        if fabs(left_point - middle) > eps or fabs(middle - right_point) > eps:
            parabola_min = find_parabola_min(function, left_point, middle, right_point)
            calls += 3
            parabola_fl = True

        if (parabola_fl and parabola_min is not None and fabs(parabola_min - left_point) < eps and fabs(right_point - parabola_min) < eps
                and fabs(parabola_min - middle) < prev_prev_len / 2):
            inner_point = parabola_min
            current_len = fabs(inner_point - middle)

        else:
            if middle <= (right_bound + left_bound) / 2:
                inner_point = middle + const * (right_bound - middle)
                current_len = right_bound - middle

            else:
                inner_point = middle + const * (left_bound - middle)
                current_len = middle - left_bound

            if fabs(inner_point - middle) < eps:
                inner_point = middle + eps if inner_point - middle > 0 else middle - eps

            inner_result = function(inner_point)
            calls += 1

            if inner_result <= middle_result:
                if inner_point >= middle:
                    left_bound = middle
                else:
                    right_bound = middle

                right_point, left_point, middle = left_point, middle, inner_point
                right_result, left_result, middle_result = left_result, middle_result, inner_result

            else:
                if inner_point >= middle:
                    right_bound = inner_point
                else:
                    left_bound = inner_point

                if inner_result <= left_result or left_point == middle:
                    right_point, left_point = left_point, inner_point
                    right_result, left_result = left_result, inner_result

                elif inner_result <= right_result or right_point == middle:
                    right_point, right_result = inner_point, middle_result

    segments.append([min(left_bound, right_bound), max(left_bound, right_bound)])
    return (segments[-1][0] + segments[-1][1]) / 2, calls, segments
