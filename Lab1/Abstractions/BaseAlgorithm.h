#ifndef BASEALGORITHM_H
#define BASEALGORITHM_H
#include "BaseFunc.h"

class BaseAlgorithm {
    virtual double GetMin(const BaseFunc& func, double leftBound, double rightBound, double eps) = 0;
};

#endif //BASEALGORITHM_H
