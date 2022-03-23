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

    segments.append((rightBound + leftBound) / 2)
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

    segments.append((rightBound + leftBound) / 2)
    return segments

def GetFibonacciNumber(n):
    return -1 / math.sqrt(5) * pow((1 - math.sqrt(5)) / 2, n) + 1 / math.sqrt(5) * pow((1 + math.sqrt(5)) / 2, n)

def FibonacciAlgorithm(leftBound, rightBound, eps):
    segments = []

    iterationNumber = 1
    fibonacciNumber_n = 1
    while fibonacciNumber_n <= (rightBound - leftBound) / eps:
        iterationNumber += 1
        fibonacciNumber_n = GetFibonacciNumber(iterationNumber)
    
    fibonacciNumber_n_minus_1 = GetFibonacciNumber(iterationNumber - 1)
    fibonacciNumber_n_minus_2 = fibonacciNumber_n - fibonacciNumber_n_minus_1

    leftPoint = leftBound + (rightBound - leftBound) * fibonacciNumber_n_minus_2 / fibonacciNumber_n
    rightPoint = leftBound + (rightBound - leftBound) * fibonacciNumber_n_minus_1 / fibonacciNumber_n

    leftResult = Function(leftPoint)
    rightResult = Function(rightPoint)

    for i in range(iterationNumber, 1, -1):
        segments.append((min(leftBound, rightBound), max(leftBound, rightBound)))

        if abs(rightBound - leftBound) < eps:
            segments.append((max(leftBound, rightBound) + min(leftBound, rightBound)) / 2)
            return segments

        if leftResult < rightResult:
            rightBound = rightPoint

            rightPoint = leftPoint
            rightResult = leftResult

            leftPoint = leftBound + (rightBound - rightPoint)
            leftResult = Function(leftPoint)
        else:
            leftBound = leftPoint

            leftPoint = rightPoint
            leftResult = rightResult

            rightPoint = rightBound + (leftBound - leftPoint)
            rightResult = Function(rightPoint)

    segments.append((max(leftBound, rightBound) + min(leftBound, rightBound)) / 2)
    return segments

def ParabolaAlgorithm(leftBound, rightBound, eps):
    segments = []
    middle = (rightBound + leftBound) / 2

    while abs(rightBound - leftBound) > eps:
        segments.append((leftBound, rightBound))

        leftResult = Function(leftBound)
        middleResult = Function(middle)
        rightResult = Function(rightBound)

        if leftResult < middleResult:
            rightBound = middle
        elif rightResult < middleResult:
            leftBound = middle
        else:
            break

    leftPoint = leftBound
    innerPoint = middle
    rightPoint = rightBound
    while innerPoint - leftPoint > eps and rightPoint - innerPoint > eps:
        segments.append((leftPoint, rightPoint))

        leftResult = Function(leftPoint)
        innerResult = Function(innerPoint)
        rightResult = Function(rightPoint)

        a1 = (innerResult - leftResult) / (innerPoint - leftPoint)
        a2 = 1 / (rightPoint - innerPoint) * ((rightResult - leftResult) / (rightPoint - leftPoint) - (innerResult - leftResult) / (innerPoint - leftPoint))

        minPoint = 1.0 / 2.0 * (leftPoint + innerPoint - a1 / a2)

        if leftPoint < minPoint and minPoint < innerPoint:
            rightPoint = innerPoint
            innerPoint = minPoint
        elif innerPoint < minPoint and minPoint < rightPoint:
            leftPoint = innerPoint
            innerPoint = minPoint
        else:
            segments.append(innerPoint)
            return segments

    segments.append(innerPoint)
    return segments


print("DichotomyAlgorithm:")
segments = DichotomyAlgorithm(3, 6, 1e-8)
print(len(segments), segments[len(segments) - 1])
print(segments, "\n")

print("GoldenRatioAlgorithm:")
segments = GoldenRatioAlgorithm(3, 6, 1e-8)
print(len(segments), segments[len(segments) - 1])
print(segments, "\n")

print("FibonacciAlgorithm:")
segments = FibonacciAlgorithm(3, 6, 1e-8)
print(len(segments), segments[len(segments) - 1])
print(segments, "\n")

print("ParabolaAlgorithm:")
segments = ParabolaAlgorithm(3, 6, 1e-8)
print(len(segments), segments[len(segments) - 1])
print(segments, "\n")