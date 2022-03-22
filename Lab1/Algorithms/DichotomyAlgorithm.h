#ifndef LAB1_DICHOTOMYALGORITHM_H
#define LAB1_DICHOTOMYALGORITHM_H
#include "..\Abstractions\IAlgorithm.h"
#include <vector>

class DichotomyAlgorithm : public IAlgorithm {
public:
    double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) override {
        _lengths.push_back(std::abs(rightBound - leftBound));

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
