#include <utility>
#include <cmath>
#include <iostream>

using zeros = std::pair<double, double>;
using solution = std::pair<bool, zeros>;

solution solveQuadratic(double a, double b, double c) {
    double check = b * b - 4 * a * c;

    if (not (check >= 0)) {
        return solution{false, zeros{0, 0}};
    } else {
        double ans1 = (-b + std::sqrt(check)) / (2 * a);
        double ans2 = (-b - std::sqrt(check)) / (2 * a);
        return solution{true, zeros{ans1, ans2}};
    }
}

int main() {
    double a, b, c;

    std::cin >> a;
    std::cin >> b;
    std::cin >> c;

    auto result = solveQuadratic(a, b, c);

    if (result.first) {
        auto [r1, r2] = result.second;
        std::cout << "the answer is " << r1 << " and " << r2 << std::endl;
    } else {
        std::cout << "no answer" << std::endl;
    }

    return 0;
}
