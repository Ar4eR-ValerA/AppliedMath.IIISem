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

def GoldenRatioAlgorithm(leftBound, rightBound, eps):
    goldenRatio = (math.sqrt(5) + 1) / 2
    segments = []

    while rightBound - leftBound > eps:
        segments.append((leftBound, rightBound))

        leftPoint = rightBound - (rightBound - leftBound) / goldenRatio
        rightPoint = leftBound + (rightBound - leftBound) / goldenRatio

        leftResult = Function(leftPoint)
        rightResult = Function(rightPoint)

        if leftResult < rightResult:
            rightBound = rightPoint
        else:
            leftBound = leftPoint

    return segments

print("DichotomyAlgorithm:")
print(DichotomyAlgorithm(3, 6, 1e-8))

print("GoldenRatioAlgorithm")
print(GoldenRatioAlgorithm(3, 6, 1e-8))