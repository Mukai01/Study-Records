#include <iostream>
#include <vector>
using std::cout;
using std::vector;

// constで引数を渡すと、誤って変更されることを防ぐことが可能
int sum(const vector<int> &v) {
    int sum = 0;
    for (int i:v)
        sum += i;
        // v[0] = 100; このように変更することはできない
        return sum;
}

int main() {
   vector<int> v {0,1,2,3,4};
   cout << sum(v) << "\n";
}