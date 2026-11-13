#include <iostream>
#include <iomanip>
#include <string>
int main()
{

    int count{0}; // count the number of prime number;
    int p{2};

    std::cout << std::left << std::setw(10) << "n"
              << std::setw(15) << "n-th prime" << std::endl;
    std::cout << std::string(25, '-') << std::endl;
    while (count < 20)
    {
        bool IsPrime = true;
        for (int i = 2; i < p; i++)
        {
            if (p % i == 0)
            {
                IsPrime = false;
                break;
            }
        }

        if (IsPrime == true)
        {
            count++;
            std::cout << std::left << std::setw(10) << count << std::setw(15) << p << std::endl;
        }
        p++;
    }

    return 0;
}