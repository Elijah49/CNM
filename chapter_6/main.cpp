#include <iostream>

double C2F(double c)
{
    return c * 9.0 / 5.0 + 32.0;
}

double F2C(double f)
{
    return (f - 32.0) * 5.0 / 9.0;
}
int main()
{
    int choice = 0;
    double T = 0;
    while (true)
    {
        std::cout << "Please choose conversion direction: " << std::endl;
        std::cout << "    1) Celsius --> Fahrenheit" << std::endl;
        std::cout << "    2) Fahrenheit --> Celsius" << std::endl;
        if (std::cin >> choice && (choice == 1 || choice == 2))
        {
            break;
        }
    }

    std::cout << "Please input the temperature: " << std::endl;

    while (!(std::cin >> T))
    {
        std::cout << "invalid input, please input again" << std::endl;
    }

    if (choice == 1)
        std::cout << T << " °C = "
                  << C2F(T) <<" °F"<<std::endl;
    else 
        std::cout << T << " °F = "
                  << F2C(T) <<" °C"<<std::endl;
    return 0;
}