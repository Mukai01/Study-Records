#include <iostream>
using std::cout;

int main() {
    int i = 1;

    // iへの参照を宣言する
    // ＆を左につけることで参照可能
    int& j = i;
    cout << "The value of j is: " << j << "\n";

    // iの値を変更する
    i = 5;
    cout << "The value of i is changed to: " << i << "\n";
    cout << "The value of j is now: " << j << "\n";

    // 参照の値を変更する。
    // 参照は変数の別名に過ぎない
    j = 7;
    cout << "The value of j is now: " << j << "\n";
    cout << "The value of i is changed to: " << i << "\n";
    }

