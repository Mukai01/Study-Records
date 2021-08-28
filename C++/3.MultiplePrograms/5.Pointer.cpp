#include <iostream>
#include <vector>
using std::cout;
using std::vector;

void AddOne(int* j)
{
    // ポインタをデリファレンスして、指されているintをインクリメントする。
    (*j)++;
}

// アドレスを返すことも可能
int* AddOne2(int& j) 
{
    // 参照されているintをインクリメントし、
    // jのアドレスを返す。
    j++;
    return &j;
}

int main() {
    // ベクトル v を宣言し、{1, 2, 3} に初期化
    vector<int> v {1, 2, 3};

    // v のアドレスへのポインタを宣言・初期化
    vector<int> *pv = &v;

    // vへのポインタをデリファレンスし、1番目を表示
    cout << (*pv)[0]<<"\n";

    // AddOne関数を使った検証 
    int i = 1;

    // i へのポインタを宣言する
    int* pi = &i;
    AddOne(pi);
    cout << "The value of i is now: " << i << "\n";

    // AddOne2関数を使った検証
    int* my_pointer = AddOne2(i);
    cout << "The value of i is now: " << i << "\n";
    cout << "The value of the int pointed to by my_pointer is: " << *my_pointer << "\n";
}
