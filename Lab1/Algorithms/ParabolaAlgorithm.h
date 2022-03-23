#ifndef LAB1_PARABOLAALGORITHM_H
#define LAB1_PARABOLAALGORITHM_H
#include "..\Abstractions\IAlgorithm.h"
#include <cmath>

class ParabolaAlgorithm : IAlgorithm {
public:
    double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) override {
        _lengths.push_back(std::fabs(rightBound - leftBound));

        double middle = (rightBound + leftBound) / 2;

        if (fabs(rightBound - leftBound) < eps) {
            return middle;
        }

        double leftResult = func.GetResult(leftBound);
        double middleResult = func.GetResult(middle);
        double rightResult = func.GetResult(rightBound);

        if (leftResult < middleResult) {
            return GetMin(func, leftBound, middle, eps);
        }
        else if (rightResult < middleResult) {
            return GetMin(func, middle, rightBound, eps);
        }
        else {
            return GetMin(func, leftBound, middle, rightBound, eps);
        }
    }

private:
    double GetMin(const IFunc& func, double leftPoint, double innerPoint, double rightPoint, double eps) {
        _lengths.push_back(fabs(rightPoint - leftPoint));

        if (innerPoint - leftPoint < eps) {
            return innerPoint;
        }

        if (rightPoint - innerPoint < eps) {
            return innerPoint;
        }

        double leftResult = func.GetResult(leftPoint);
        double innerResult = func.GetResult(innerPoint);
        double rightResult = func.GetResult(rightPoint);

        double a1 = (innerResult - leftResult) / (innerPoint - leftPoint);
        double a2 = 1 / (rightPoint - innerPoint) * (
                (rightResult - leftResult) / (rightPoint - leftPoint) -
                (innerResult - leftResult) / (innerPoint - leftPoint));

        double minPoint = 1.0 / 2.0 * (leftPoint + innerPoint - a1 / a2);

        if (leftPoint < minPoint && minPoint < innerPoint) {
            return GetMin(func, leftPoint, minPoint, innerPoint, eps);
        }
        else if (innerPoint < minPoint && minPoint < rightPoint) {
            return GetMin(func, innerPoint, minPoint, rightPoint, eps);
        }
        else {
            return innerPoint;
        }
    }
};

#endif //LAB1_PARABOLAALGORITHM_H
