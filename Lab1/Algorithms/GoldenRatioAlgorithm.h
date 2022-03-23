#ifndef LAB1_GOLDENRATIOALGORITHM_H
#define LAB1_GOLDENRATIOALGORITHM_H
#include "..\Abstractions\BaseAlgorithm.h"
#include <cmath>

class GoldenRationAlgorithm : public BaseAlgorithm {
public:
    double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) override {
        _segments.push_back({std::min(leftBound, rightBound), std::max(leftBound, rightBound)});

        if (rightBound - leftBound < eps) {
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

private:
    double GoldenRatio = (sqrt(5) + 1) / 2;
};

#endif //LAB1_GOLDENRATIOALGORITHM_H
