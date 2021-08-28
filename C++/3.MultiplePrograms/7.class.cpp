#include <iostream>
#include <string>
using std::string;
using std::cout;

// Classの設定
class Car {
  public:
    void PrintCarData() 
    {
        std::cout << "The distance that the " << color << " car " << number << " has traveled is: " << distance << "\n";
    }

    void IncrementDistance() 
    {
        distance++;
    }
    
    // ここにコンストラクタを追加:
    Car(string c, int n) 
    {
        // コンストラクタに渡された値でクラスの属性を設定。
        color = c;
        number = n;
    }
    
    std::string color;
    int distance = 0;
    int number;
};

int main() {
    // 各車のクラスのインスタンスを作成。
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