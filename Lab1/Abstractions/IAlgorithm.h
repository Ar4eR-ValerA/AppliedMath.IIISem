#ifndef BASEALGORITHM_H
#define BASEALGORITHM_H
#include<vector>

#include "IFunc.h"

class IAlgorithm {
    virtual double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) = 0;
    std::vector<double> GetVec() {
        return _lengths;
    }

protected:
    std::vector<double> _lengths;
};

#endif //BASEALGORITHM_H
