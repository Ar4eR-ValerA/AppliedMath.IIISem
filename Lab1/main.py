import math

def Function(x):
    return math.sin(x) * math.pow(x, 3)

def DichotomyAlgorithm(leftBound, rightBound, eps):
    segments = []

    while rightBound - leftBound > eps:
        segments.append((leftBound, rightBound))

        middle = (leftBound + rightBound) / 2

        leftResult = Function(middle - eps)
        rightResult = Function(middle + eps)

        if leftResult < rightResult:
            rightBound = middle
        else:
            leftBound = middle

    return segments

print(DichotomyAlgorithm(3, 6, 1e-8))