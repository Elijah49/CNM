#include <iostream>
#include <fstream>
#include <iomanip>

int main()
{
    const double m = 65;
    const double g = 9.81;
    const double c = 13;
    const double h = 0.5;
    const int NoS=100;
    double v{0};

    std::ofstream f_out{"5_8.txt"};
        if (!f_out.good())
    {
        std::cout << "the file open failed" << std::endl;
        return 1;
    }

    for (int i=0;i<=NoS;i++)
    {
        f_out<<std::left<<std::setw(10)<<
            i*h<<v<<std::endl;
        v=v+(g-c/m*v)*(h);

    }
    std::cout<<"using time step = "<< h
        << " the velocity at t = "<<h*NoS<<" is equals to "
        << v <<" m/s"; 

    

    return 0;
}