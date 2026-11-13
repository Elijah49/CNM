#include <iostream>
#include <cstdlib>
#include <ctime>

namespace UD
{
    double max(const double* start_pointer)
    {
        double max=*start_pointer;
        for (int i=0;i<100;i++)
        {
            if (*(start_pointer+i)>=max) max=*(start_pointer+i);
        }
        return max;
    }

    double min(const double* start_pointer)
    {
        double min=*start_pointer;
        for (int i=0;i<100;i++)
        {
            
            if (*(start_pointer+i)<=min) min=*(start_pointer+i);
        }
        return min;
    }

    double average(const double* start_pointer)
    {
        double average{0};
        for (int i=0;i<100;i++)
        {
            average+=*(start_pointer+i);
        }
        return average/100.0;        
    }
    
}

int main()
{
    double arr_rand[100];
    unsigned int x{0};
    std::cout<<"Please input an integer number as seed";
    std::cin>>x;
    std::srand(x);
    std::srand(static_cast<unsigned int>(std::time(0)));



    for (int i=0; i<100 ;i++)
    {
        arr_rand[i]=static_cast<double>(std::rand())/RAND_MAX*100;
        std::cout<<arr_rand[i]<<" ";
    }
    std::cout<<std::endl;
    std::cout<<"The maximum value of this random array is: "<< UD::max(&arr_rand[0])<<std::endl;
    std::cout<<"The minimum value of this random array is: "<< UD::min(&arr_rand[0])<<std::endl;
    std::cout<<"The average value of this random array is: "<< UD::average(&arr_rand[0])<<std::endl;

 


    return 0;
}