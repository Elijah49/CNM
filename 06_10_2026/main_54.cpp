#include <iostream>
#include <string>
int main()
{
    long int result{1};
    std::string input{""};
    int n{0};
    std::cout << "please input the number n";
    std::getline(std::cin, input);
    n = std::stoi(input);
    if (n == 0)
        ;
    else
        for (int i = n; i > 0; i--)
        {
            result *= i;
        }
    std::cout << result << std::endl;
    return 0;

}