#include <iostream>
#include <vector>
using std::vector;
using std::cout;

int main() {
    // vectorの定義方法
    vector<int> v_1{0,1,2};
    vector<int> v_2{3,4,5};
    vector<int> v_3;
    v_3={6};
    cout << "Everything Worked\n";

    //2次元ベクトル定義 
    vector<vector<int>> v{{1,2},{3,4}};
    cout << "2D Vector has been created";
}