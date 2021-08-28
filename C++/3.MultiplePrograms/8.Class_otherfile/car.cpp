#include <iostream>
#include "car.h"

// 別ファイルの時はCarクラスであることを示す必要がある
void Car::PrintCarData() 
{
    cout << "The distance that the " << color << " car " << number << " has traveled is: " << distance << "\n";
}

void Car::IncrementDistance() 
{
    distance++;
}