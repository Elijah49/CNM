#include <iostream>
void swap(int &a, int &b)
{
    int temp;
    temp=a;
    a=b;
    b=temp;
}
int main()
{
    int x{0};
    int y{0};
    int z{0};
    std::cin>>x;
    std::cin>>y;
    std::cin>>z;
    if (x>y) swap(x,y);
    if (y>z) swap(y,z);
    if (x>z) 
    swap(x,y);
    std::cout<<x<<" "<<y<<std::endl;
    return 0;
}