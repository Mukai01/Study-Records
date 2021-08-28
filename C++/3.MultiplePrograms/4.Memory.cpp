#include <iostream>
using std::cout;

int main() {
    int i = 5;
    int j = 6;

    // iとjのメモリアドレスを印刷
    // 変数は内容をメモリに保存する、そのメモリのアドレスを表示可能
    // &　は方程式の左にあるときは参照、右にある時はアドレスを返す
    cout << "The address of i is: " << &i << "\n";
    cout << "The address of j is: " << &j << "\n";

    // ポインタを宣言するときは、*を使用する
    int* pointer_to_i = &i;
    cout << "The variable pointer_to_i is: " << pointer_to_i << "\n";

    // *を右辺で使うと、オブジェクトを返す
    cout << "The value of the variable pointed to by pointer_to_i is: " << *pointer_to_i << "\n";

    // i の値が変更された。
    i = 7;
    cout << "The new value of the variable i is                     : " << i << "\n";
    cout << "The value of the variable pointed to by pointer_to_i is: " << *pointer_to_i << "\n";
    }
