#include <iostream>
#include <iterator>//to support std::size
int main()
{
    unsigned int N;
    std::cout << "Please input the number of primes" << std::endl;
    std::cin >> N;
    int* Primes_arr {new int [N]{}};
    int count{};
    int candidate{2};
    while (count<static_cast<int>(N))
    {
        bool isPrime=true;
        for (int i=0;i<count ; i++)
        {
            if (Primes_arr[i]*Primes_arr[i]>candidate) break;
            if (candidate % Primes_arr[i]==0) {isPrime = false; break;}
        }
        if (isPrime) Primes_arr[count++]=candidate;
        candidate++;
    }
    for (int i = 0; i < static_cast<int>(N); i++)
    {
        std::cout << Primes_arr[i] << ' ';
    }

    delete[] Primes_arr;
    return 0;
}