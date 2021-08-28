#include <iostream>
#include <string>
#include "car.h"
using std::string;
using std::cout;

int main() {
    // 各車のクラスインスタンスを作成。
    Car car_1 = Car("green", 1);
    Car car_2 = Car("red", 2);
    Car car_3 = Car("blue", 3);

    // car_1の位置を1だけ増やす。
    car_1.IncrementDistance();

    // 各車の位置と色を印刷する。
    car_1.PrintCarData();
    car_2.PrintCarData();
    car_3.PrintCarData();
}