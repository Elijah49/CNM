#include <iostream>
#include <cmath>

double f(double x);
double simpson(double a, double b, int n);
int main()
{
    double a{-1};
    double b{1};
    int n{0};
    while (true)
    {
        std::cout << "please input an even number" << std::endl;
        std::cin >> n;
        if (n % 2 == 0 && n > 0)
            break;
        else
            std::cerr << "Invalid input, n must be an even number" << std::endl;
    }

    std::cout << "The result of integral equals to: " << simpson(a, b, n);
    return 0;
}

double f(double x)
{
    return x * x * std::exp(std::pow(x, 2));
}

double simpson(double a, double b, int n)
{
    double result{(b - a) / (3.0 * n)};
    double sum{0};
    double h = (b - a) / n;
    for (int i = 1; i < n; i++)
    {
        if (i % 2 == 1)
            sum += 4 * f(a + i * h);
        else
            sum += 2 * f(a + i * h);
    }
    result *= sum + f(a) + f(b);
    return result;
}