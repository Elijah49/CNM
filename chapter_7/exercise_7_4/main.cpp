#include <iostream>
#include <ctime>
void insert(double a[], int p, double val)
{
    int marker_index = p;
    while (marker_index >= 0 && a[marker_index] > val)
    {
        a[marker_index + 1] = a[marker_index];
        marker_index--;
    }
    a[marker_index + 1] = val;
}

void insertionSort(double a[], int l)
{
    for (int i = 0; i < l - 1; i++)
    {
        insert(a, i, a[i + 1]);
    }
}
int main()
{
    const int n{20};
    const int range{100};
    double a[n];

    srand(static_cast<unsigned int>(time(0)));
    std::cout << "Generate random numbers" << std::endl;
    for (int i = 0; i < n; i++)
    {
        a[i] = static_cast<double>(rand()) / RAND_MAX * range;
        std::cout << a[i] << ' ';
    }
    std::cout << std::endl;
    insertionSort(a, 20);
    for (double e : a)
        std::cout << e << ' ';
    return 0;
}
