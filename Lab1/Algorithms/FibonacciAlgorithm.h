#ifndef LAB1_FIBONACCIALGORITHM_H
#define LAB1_FIBONACCIALGORITHM_H
#include "..\Abstractions\BaseAlgorithm.h"
#include <cmath>

class FibonacciAlgorithm : public BaseAlgorithm {
public:
    double IterationsNumber;
    double FibonacciNumber_n;
    double FibonacciNumber_n_minus_1;
    double FibonacciNumber_n_minus_2;

    FibonacciAlgorithm(int iterationsNumber) {
        IterationsNumber = iterationsNumber;

        double n = iterationsNumber;
        FibonacciNumber_n_minus_1 = -1 / sqrt(5) * pow((1 - sqrt(5)) / 2, n - 1) + 1 / sqrt(5) * pow((1 + sqrt(5)) / 2, n - 1);
        FibonacciNumber_n_minus_2 = -1 / sqrt(5) * pow((1 - sqrt(5)) / 2, n - 2) + 1 / sqrt(5) * pow((1 + sqrt(5)) / 2, n - 2);
        FibonacciNumber_n = FibonacciNumber_n_minus_1 + FibonacciNumber_n_minus_2;
    }

    double GetMin(const BaseFunc& func, double leftBound, double rightBound, double eps) override {
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
};


#endif //LAB1_FIBONACCIALGORITHM_H
