#ifndef LAB1_DICHOTOMYALGORITHM_H
#define LAB1_DICHOTOMYALGORITHM_H
#include "..\Abstractions\BaseAlgorithm.h"
#include <vector>

class DichotomyAlgorithm : public BaseAlgorithm {
public:
    double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) override {
        _segments.push_back({std::min(leftBound, rightBound), std::max(leftBound, rightBound)});

        double middle = (leftBound + rightBound) / 2;

        if (rightBound - leftBound < eps) {
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
