#include <iostream>
#include <string>
#include <cmath>
int main()
{
    std::string input;
    double radius;
    double volume;
    double area;
    int a;
    std::cout << "Please enter the radius of the sphere: ";
    while (true)
    {
        std::getline(std::cin, input);
        radius = std::stod(input);
        if (radius < 0)
        {
            std::cout << "Invalid input. Please enter a non-negative number for the radius: ";
        }
        break; // Valid input, exit the loop
    }
    radius = std::stod(input);
    volume = (4.0 / 3.0) * M_PI * std::pow(radius, 3);
    area = 4.0 * M_PI * pow(radius, 2);
    std::cout << "The volume of the sphere is: " << volume << std::endl;
    std::cout << "The area of the sphere is: " << area << std::endl;
    return 0;
}