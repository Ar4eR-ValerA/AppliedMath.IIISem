#ifndef LAB1_BRENTALGORITHM_H
#define LAB1_BRENTALGORITHM_H
#include "..\Abstractions\BaseAlgorithm.h"
#include <cmath>

class BrentAlgorithm : public BaseAlgorithm {
public:
    double GetMin(const BaseFunc& func, double leftBound, double rightBound, double eps) override {
        double middle = (leftBound + rightBound) / 2;
        double leftPoint = middle, rightPoint = middle;

        double middleResult = func.GetResult(middle);
        double leftResult = middleResult, rightResult = middleResult;

        double prevStepLength = rightBound - leftBound;
        double currentStepLength = rightBound - leftBound;

        eps /= 10;
        while (fabs(rightBound - leftBound) >= 10 * eps) {
            double innerPoint;
            double prevPrevStepLength = prevStepLength;
            prevStepLength = currentStepLength;

            double parabolaMin;
            bool parabolaFl = false;
            if (fabs(leftPoint - middle) > eps || fabs(middle - rightPoint) > eps) {
                parabolaMin = ParabolaMin(func, leftPoint, middle, rightPoint);
                parabolaFl = true;
            }

            if (parabolaFl
            && parabolaMin >= leftPoint + eps
            && parabolaMin <= rightPoint - eps
            && fabs(parabolaMin - middle) < prevPrevStepLength / 2) {
                innerPoint = parabolaMin;
                currentStepLength = fabs(innerPoint - middle);
            }
            else {
                if (middle <= (rightBound + leftBound) / 2) {
                    innerPoint = middle + K * (rightBound - middle);
                    currentStepLength = rightBound - middle;
                }
                else {
                    innerPoint = middle + K * (leftBound - middle);
                    currentStepLength = middle - leftBound;
                }

                if (fabs(innerPoint - middle) < eps) {
                    if (innerPoint - middle > 0) {
                        innerPoint = middle + eps;
                    }
                    else {
                        innerPoint = middle - eps;
                    }
                }

                double innerResult = func.GetResult(innerPoint);

                if (innerResult <= middleResult) {
                    if (innerPoint >= middle) {
                        leftBound = middle;
                    }
                    else {
                        rightBound = middle;
                    }

                    rightPoint = leftPoint;
                    leftPoint = middle;
                    middle = innerPoint;

                    rightResult = leftResult;
                    leftResult = middleResult;
                    middleResult = innerResult;
                }
                else {
                    if (innerPoint >= middle) {
                        rightBound = innerPoint;
                    }
                    else {
                        leftBound = innerPoint;
                    }

                    if (innerResult <= leftResult || leftPoint == middle) {
                        rightPoint = leftPoint;
                        leftPoint = innerPoint;

                        rightResult = leftResult;
                        leftResult = innerResult;
                    }
                    else if (innerResult <= rightResult || rightPoint == middle) {
                        rightPoint = innerPoint;

                        rightResult = middleResult;
                    }
                }
            }
        }

        return (leftBound + rightBound) / 2;
    }

private:
    double K = (3 - sqrt(5)) / 2;

    double ParabolaMin(const BaseFunc& func, double leftPoint, double innerPoint, double rightPoint) {
        double leftResult = func.GetResult(leftPoint);
        double innerResult = func.GetResult(innerPoint);
        double rightResult = func.GetResult(rightPoint);

        double a1 = (innerResult - leftResult) / (innerPoint - leftPoint);
        double a2 = 1 / (rightPoint - innerPoint) * (
                (rightResult - leftResult) / (rightPoint - leftPoint) -
                (innerResult - leftResult) / (innerPoint - leftPoint));

        double minPoint = 1.0 / 2.0 * (leftPoint + innerPoint - a1 / a2);
        return minPoint;
    }
};

#endif //LAB1_BRENTALGORITHM_H
