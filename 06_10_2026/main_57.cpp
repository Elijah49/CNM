#include <iostream>
#include <fstream>
int main()
{
    std::ifstream stream_input{"5_6_sin.txt"};
    if (!stream_input)
    {
        std::cerr<<"Error, could not of this file";
    }
    float x,y{0};
    while (stream_input>>x>>y)
    {
        std::cout <<std::setw(10)<<std::left<< x <<" "<< y<<std::endl;
    }

    return 0;
}