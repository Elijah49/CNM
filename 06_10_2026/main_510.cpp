#include <iostream>

int main()
{
    int Number_To_Guess{40};
    int User_Input{0};
    while (true)
    {
        std::cout<<"Please input the number you guess"<<std::endl;
        std::cin>>User_Input;
        if (User_Input==Number_To_Guess)
        {
            std::cout<<"You Win!";
            break;
        }
        else if (User_Input>Number_To_Guess)
            std::cout<<"Too High"<<std::endl;
        else 
            std::cout<<"Too Low"<<std::endl;
    }
    return 0;
}