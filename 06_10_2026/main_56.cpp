#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream> //output to .txt

int main()
{
    std::ofstream outFile("5_6_sin.txt");
    if (!outFile.good())
    {
        std::cout << "the file open failed" << std::endl;
        return 1;
    }

    double c = 2 * M_PI / 100;
   //outFile << std::left << std::setw(10) << 'i' << std::setw(15) << "sin" << std::endl;
    for (int i = 0; i < 100; i++)
    {
        outFile <<std::setprecision(5)<< std::left << std::setw(10) << i*c << std::setw(15) << sin(c * i) << std::endl;
    }
    outFile.close();
    return 0;
}