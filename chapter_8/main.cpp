#include <iostream>
#include <array>
int main()
{
    std::array<int,3> arr{1,2,3};
    int* ptr = arr.data();
    std::cout << *ptr <<std::endl;

}