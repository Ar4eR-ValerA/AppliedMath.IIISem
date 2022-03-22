#ifndef LAB1_PARABOLAALGORITHM_HPP
#define LAB1_PARABOLAALGORITHM_HPP
#include "..\Abstractions\BaseAlgorithm.h"
#include <cmath>

class ParabolaAlgorithm : BaseAlgorithm {
    double GetMin(const BaseFunc& func, double leftBound, double rightBound, double eps) override {
        double middle = (rightBound - leftBound) / 2;

        if (fabs(rightBound - leftBound) < eps) {
            return middle;
        }

        // TODO: Сделать проверку на то f1 > f2 < f3, если нет, то вызывать заново с новыми промежутками.
        // TODO: Сделать ещё одну рекурсивную функцию, в которую можно вводить middle точку.
        return 0;
    }
};

#endif //LAB1_PARABOLAALGORITHM_HPP
