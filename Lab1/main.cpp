#include <iostream>
#include "Functions\Sinx_x3.h"
#include "Algorithms\DichotomyAlgorithm.h"
#include "Algorithms\GoldenRatioAlgorithm.h"
#include "Algorithms\FibonacciAlgorithm.h"
#include "Algorithms\ParabolaAlgorithm.h"
#include "Algorithms\BrentAlgorithm.h"

int main() {
    Sinx_x3 func;
    double leftBound, rightBound, eps;

    std::cout << "Enter left bound, right bound, precision (number of digits after decimal point)\n";
    std::cin >> leftBound >> rightBound >> eps;
    std::cout.precision(fabs(eps));

    DichotomyAlgorithm dichotomyAlgorithm;
    std::cout << "DichotomyAlgorithm:\n";
    std::cout << dichotomyAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    GoldenRationAlgorithm goldenRationAlgorithm;
    std::cout << "\nGoldenRationAlgorithm:\n";
    std::cout << goldenRationAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    FibonacciAlgorithm fibonacciAlgorithm;
    std::cout << "\nFibonacciAlgorithm:\n";
    std::cout << fibonacciAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    ParabolaAlgorithm parabolaAlgorithm;
    std::cout << "\nParabolaAlgorithm:\n";
    std::cout << parabolaAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    BrentAlgorithm brentAlgorithm;
    std::cout << "\nBrentAlgorithm:\n";
    std::cout << brentAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    return 0;
}
