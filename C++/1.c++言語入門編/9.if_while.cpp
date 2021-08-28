#include <iostream>
using std::cout;

int main() {
    // if文
    bool a = true;

    if (a) {
        cout << "You made it into the if statement\n";
    }

    //while文 
    auto i = 0;
    while (i < 5) {
        cout << i << "\n";
        i++;
    }

    // whileとif文の組み合わせ
    // 偶数のみprint
    auto n = 0;
    while (n < 10) {
        int remainder = n % 2;
        if (remainder == 0){
            cout << n << "\n";
        }
        n++;
    }
}
