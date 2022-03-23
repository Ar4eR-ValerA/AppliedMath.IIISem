#ifndef LAB1_FIBONACCIALGORITHM_H
#define LAB1_FIBONACCIALGORITHM_H
#include "..\Abstractions\BaseAlgorithm.h"
#include <cmath>

class FibonacciAlgorithm : public BaseAlgorithm {
public:
    double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) override {
        _segments.push_back({std::min(leftBound, rightBound), std::max(leftBound, rightBound)});

        int IterationsNumber = 1;
        long long FibonacciNumber_n = 1;
        while (FibonacciNumber_n <= (rightBound - leftBound) / eps) {
            IterationsNumber++;
            FibonacciNumber_n = GetFibonacciNumber(IterationsNumber);
        }
        long long FibonacciNumber_n_minus_1 = GetFibonacciNumber(IterationsNumber - 1);
        long long FibonacciNumber_n_minus_2 = FibonacciNumber_n - FibonacciNumber_n_minus_1;

        double leftPoint = leftBound + (rightBound - leftBound) * FibonacciNumber_n_minus_2 / FibonacciNumber_n;
        double rightPoint = leftBound + (rightBound - leftBound) * FibonacciNumber_n_minus_1 / FibonacciNumber_n;

        double leftResult = func.GetResult(leftPoint);
        double rightResult = func.GetResult(rightPoint);

        for (int i = IterationsNumber - 1; i > 1; --i) {
            if (fabs(rightBound - leftBound) < eps) {
                return (rightBound + leftBound) / 2;
            }

            if (leftResult < rightResult) {
                rightBound = rightPoint;

                rightPoint = leftPoint;
                rightResult = leftResult;

                leftPoint = leftBound + (rightBound - rightPoint);
                leftResult = func.GetResult(leftPoint);
            }
            else {
                leftBound = leftPoint;

                leftPoint = rightPoint;
                leftResult = rightResult;

                rightPoint = rightBound + (leftBound - leftPoint);
                rightResult = func.GetResult(rightPoint);
            }
        }

        return (rightBound + leftBound) / 2;
    }

private:
    long long GetFibonacciNumber(int n) {
        return round(
                -1 / sqrt(5) * pow((1 - sqrt(5)) / 2, n)
                +1 / sqrt(5) * pow((1 + sqrt(5)) / 2, n));
    }
};


#endif //LAB1_FIBONACCIALGORITHM_H
