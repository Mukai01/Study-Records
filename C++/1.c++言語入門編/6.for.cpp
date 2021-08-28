#include <iostream>
#include <vector>
using std::cout;
using std::vector;

int main() {
    // forループ
    for (int i=0; i<5; i++) {
        cout<< i<< "\n";
    };

    // ++はインクリメント演算子という
    // プリインクリメントとポストインクリメントがある
    auto i = 1;
    auto c = i++; //ポストインクリメント
    cout<< "increment..." <<"\n";
    cout << "c:" << c << "\n"; //演算子が使われた後にインクリメント
    cout << "i:" << i << "\n";

    i = 1; 
    c = ++i; //プリインクリメント
    cout << "c:" << c << "\n"; //演算子が使われた際にインクリメント
    cout << "i:" << i << "\n";

    // コンテナを使うforループ
    vector<int> a{1,2,3,4,5};
    cout<< "for roop by container" <<"\n";
    for (int i : a) {
        cout<< i<< "\n";
    };

    // 2次元ベクトルを使うforループ
    vector<vector<int>> b{{1,2},{3,4},{5,6}};
    cout<< "for roop by 2d-vector" <<"\n";
    for (vector<int> i : b) {
        for (int j : i) {
                cout<< j<< "\n";
        };
    };
}
