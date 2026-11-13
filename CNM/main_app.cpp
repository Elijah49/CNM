
#include <iostream>

int main(int argc, char **argv)
{
    int vNum = 3;
    std::cout << "Hello, World!" << std::endl;
    bool vTest = true;
    
    if (vTest)

    {
        for (int i = 0; i < 10; ++i)
        {
            vNum++;
        }
    }
    std::cout << "The boolean is: " << vTest;
    return 0;
}
