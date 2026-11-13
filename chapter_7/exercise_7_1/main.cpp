#include <iostream>
#include <cstdlib>
#include <iterator>// toc support std::size

double Min_UD(double arr[], int size);
double Max_UD(double arr[], int size);
double Average_UD(double arr[], int size);
int main()
{
    double arr[100]{};
    std::cout << RAND_MAX << std::endl;
    for (int i = 0; i < 100; i++)
    {
        // 1
        // arr[i]=std::rand()%100; create any integer between 0 and 100

        // 2
        arr[i] = (100.0 * std::rand()) / RAND_MAX;
        std::cout << arr[i] << std::endl;
    }
    std::cout << "The minimum value is: " << Min_UD(arr, std::size(arr)) << std::endl;
    std::cout << "The maximum value is: " << Max_UD(arr, std::size(arr)) << std::endl;
    std::cout << "The average value is: " << Average_UD(arr, std::size(arr)) << std::endl;
    return 0;
}

double Min_UD(double arr[], int size)
{
    double min = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}

double Max_UD(double arr[], int size)
{
    double max = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

double Average_UD(double arr[], int size)
{
    double sum{0};
    for (int i=0 ; i <size ; i++)
    {
        sum += arr[i];
    }
    return sum/size;
}
