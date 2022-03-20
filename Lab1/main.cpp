#include <iostream>
#include "Functions\Sinx_x3.h"
#include "Algorithms\DichotomyAlgorithm.h"
#include "Algorithms\GoldenRatioAlgorithm.h"
#include "Algorithms\FibonacciAlgorithm.h"

int main() {
    Sinx_x3 func;
    double leftBound, rightBound, eps = 8;

    //std::cout << "Enter left bound, right bound, precision (number of digits after decimal point)\n";
    //std::cin >> leftBound >> rightBound >> eps;

    std::cin >> leftBound >> rightBound;
    std::cout.precision(fabs(eps));

    DichotomyAlgorithm dichotomyAlgorithm;
    std::cout << "DichotomyAlgorithm:\n";
    std::cout << dichotomyAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    GoldenRationAlgorithm goldenRationAlgorithm;
    std::cout << "\nGoldenRationAlgorithm:\n";
    std::cout << goldenRationAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";

    double iterationsNumber;
    std::cout << "\nEnter number of iterations\n";
    std::cin >> iterationsNumber;
    FibonacciAlgorithm fibonacciAlgorithm(iterationsNumber);
    std::cout << "\nFibonacciAlgorithm:\n";
    std::cout << fibonacciAlgorithm.GetMin(func, leftBound, rightBound, pow(10, -eps)) << "\n";
    // Функция говна, если что
    // Применение этой штуки крайне сомнительно

    return 0;
}