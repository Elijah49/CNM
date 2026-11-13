#include <iostream>
#include <cmath>
#include <iomanip>

int main()
{
    double result{0};
    int i = 0;
    while (true)
    {
        result += pow(-1, i) / (2 * i + 1);
        if ((M_PI - 4.0 * result <= 0.00004) && (M_PI - 4.0 * result >= -0.00005))
        {
            break;
        }
        else
            i += 1;
    }
    std::cout << std::setprecision(5) << result * 4.0 << " " << i<<std::endl;

    i = 1;
    result = 1;
    while (true)
    {
        result *= 4.0*pow(i,2)/(4.0*pow(i,2)-1);
        if ((M_PI - 2.0 * result <= 0.00004) && (M_PI - 2.0 * result >= -0.00005))
        {
            break;
        }
        else
            i += 1;
    }
    std::cout << std::setprecision(5) << result * 2.0 << " " << i;

    return 0;
}