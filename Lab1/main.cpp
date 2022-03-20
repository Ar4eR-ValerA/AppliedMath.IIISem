#include <iostream>
#include "Functions\Sinx_x3.h"
#include "Algorithms\DichotomyAlgorithm.h"
#include "Algorithms\GoldenRatioAlgorithm.h"

int main() {
    Sinx_x3 func;
    DichotomyAlgorithm dichotomyAlgorithm;
    GoldenRationAlgorithm goldenRationAlgorithm;

    double leftBound, rightBound, eps = 8;

    //std::cout << "Enter left bound, right bound, precision (number of digits after decimal point)\n";
    //std::cin >> leftBound >> rightBound >> eps;

    std::cin >> leftBound >> rightBound;
    std::cout.precision(fabs(eps));

    std::cout << "DichotomyAlgorithm:\n";
    std::cout << dichotomyAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";
    std::cout << "\nGoldenRationAlgorithm:\n";
    std::cout << goldenRationAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    return 0;
}