#ifndef LAB1_DICHOTOMYALGORITHM_H
#define LAB1_DICHOTOMYALGORITHM_H
#include "..\Abstractions\BaseAlgorithm.h"
#include <stdexcept>
#include <cmath>

class DichotomyAlgorithm : public BaseAlgorithm {
public:
    double GetMin(const BaseFunc& func, double leftBound, double rightBound, double eps) override {
        double middle = (leftBound + rightBound) / 2;

        if (fabs(rightBound - leftBound) < eps) {
            return middle;
        }

        double leftResult = func.GetResult(middle - eps);
        double rightResult = func.GetResult(middle + eps);

        if (leftResult < rightResult) {
            return GetMin(func, leftBound, middle, eps);
        }
        else {
            return GetMin(func, middle, rightBound, eps);
        }

    }
};

#endif //LAB1_DICHOTOMYALGORITHM_H
