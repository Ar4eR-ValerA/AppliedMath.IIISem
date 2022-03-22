#ifndef LAB1_BRENTALGORITHM_H
#define LAB1_BRENTALGORITHM_H
#include "..\Abstractions\IAlgorithm.h"
#include <cmath>

class BrentAlgorithm : public IAlgorithm {
public:
    double GetMin(const IFunc& func, double leftBound, double rightBound, double eps) override;
private:
    double K = (3 - sqrt(5)) / 2;
    double ParabolaMin(const IFunc& func, double leftPoint, double innerPoint, double rightPoint);
    std::vector<double> _lengths;
};

#endif //LAB1_BRENTALGORITHM_H
