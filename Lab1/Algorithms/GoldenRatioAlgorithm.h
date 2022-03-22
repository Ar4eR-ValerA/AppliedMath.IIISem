#ifndef LAB1_GOLDENRATIOALGORITHM_H
#define LAB1_GOLDENRATIOALGORITHM_H
#include "..\Abstractions\BaseAlgorithm.h"
#include <cmath>

class GoldenRationAlgorithm : public BaseAlgorithm {
public:
    double GoldenRatio = (sqrt(5) + 1) / 2;

    double GetMin(const BaseFunc& func, double leftBound, double rightBound, double eps) override {
        if (fabs(rightBound - leftBound) < eps) {
            return (rightBound + leftBound) / 2;
        }

        double leftPoint = rightBound - (rightBound - leftBound) / GoldenRatio;
        double rightPoint = leftBound + (rightBound - leftBound) / GoldenRatio;

        double leftResult = func.GetResult(leftPoint);
        double rightResult = func.GetResult(rightPoint);

        if (leftResult < rightResult) {
            return GetMin(func, leftBound, rightPoint, eps);
        }
        else {
            return GetMin(func, leftPoint, rightBound, eps);
        }
    }
};

#endif //LAB1_GOLDENRATIOALGORITHM_H
