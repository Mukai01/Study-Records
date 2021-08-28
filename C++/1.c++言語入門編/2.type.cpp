#include <iostream>
// stringはc++標準ライブラリであり、includeすると利用可能になる
// 名前空間はstdなので、使用のたびにstd::をするか、usingで記述しておく
#include <string>

using std::cout;
// 以下のようにusingを使っておけば、stringだけでよくなる
// using std::string;

int main() {
    int a = 9;

    std::string b;
    b = "Here is a string";
    
    cout << a << "\n";
    cout << b;
}