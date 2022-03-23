#ifndef BASEALGORITHM_H
#define BASEALGORITHM_H
#include<vector>

#include "IFunc.h"

class BaseAlgorithm {
public:
    virtual double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) = 0;

    std::vector<std::pair<double, double>> GetSegments() {
        return _segments;
    }

    void ResetSegments() {
        _segments.clear();
    }

protected:
    std::vector<std::pair<double, double>> _segments;
};

#endif //BASEALGORITHM_H
