
#include <iostream>

int main()
{
    int x = 5;
    int y = x++;
    int z = ++x;
    int a {};
    a= x++ +1;
    std::cout << y << std::endl;
    std::cout << z << std::endl;
    std::cout << a << std::endl;
    std::cout << x << std::endl;
    return 0;
}
