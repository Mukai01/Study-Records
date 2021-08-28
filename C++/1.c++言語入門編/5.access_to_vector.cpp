#include <iostream>
#include <vector>
using std::vector;
using std::cout;

int main() {
    // 1次元ベクトルへのアクセス
    vector<int> a={0,1,2,3,4};
    cout<< "access to vector..." <<"\n";
    cout<<a[0];
    cout<<a[1];
    cout<<a[2];
    cout<< "\n";

    // 2次元ベクトルへのアクセス
    vector<vector<int>> b={{1,1,2,3},
                            {2,1,2,3},
                            {3,1,2,3}};
    cout<< b[0][2];
    cout<< "\n";

    // ベクトルの長さ
    cout<< "vector length..." <<"\n";
    cout<< a.size() <<"\n";
    cout<< b[0].size() <<"\n";
}