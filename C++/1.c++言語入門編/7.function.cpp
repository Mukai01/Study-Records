#include <iostream>
#include <vector>
#include <string>
using std::cout;
using std::vector;
using std::string;

// 関数の定義
// 整数の足し算
int AdditionFunction(int i, int j){
    return i + j;
}

// ベクトルの合計
int AdditionFunction2(vector<int> v_1){
    int sum = 0;
    for (int i:v_1) {
        sum = sum + i;
    }
    return sum;
}

// 関数が何も返さなくてよい場合voidとする
void PrintStrings(string s1,string s2){
    cout << s1 + s2 << "\n";
}

// 実行部分
int main() {
    auto d = 3;
    auto f = 7;
    cout << AdditionFunction(d,f) << "\n";

    auto v = {1,2,3};
    cout << AdditionFunction2(v) << "\n";

    string s1 = "C++ is";
    string s2 = "super awesome.";
    PrintStrings(s1,s2);
}
