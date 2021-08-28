#ifndef CAR_H
#define CAR_H

#include <string>
using std::string;
using std::cout;

class Car {
  public:
    void PrintCarData();
    void IncrementDistance();
    
    // コンストラクターでイニシャライザリストを使用する（書き方が少し変わっている）
    Car(string c, int n) : color(c), number(n) {}
  
  // クラスの外部に表示する必要のない変数はprivateとして設定。クラスの外からはアクセスできない。
  private:
    string color;
    int distance = 0;
    int number;
};

#endif