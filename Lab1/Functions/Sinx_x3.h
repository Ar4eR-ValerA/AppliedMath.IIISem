#ifndef LAB1_SINX_X3_H
#define LAB1_SINX_X3_H
#include "..\Abstractions\IFunc.h"
#include <cmath>

class Sinx_x3 : public IFunc {
public:
    double GetResult(double x) const override {
        return sin(x) * pow(x, 3);
    }
};

#endif //LAB1_SINX_X3_H
