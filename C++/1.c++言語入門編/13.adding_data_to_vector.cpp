#include <vector>
#include <iostream>
using std::vector;
using std::cout;

int main() {
    vector<int> v {1, 2, 3};

    for (int i=0; i < v.size(); i++) {
    cout << v[i] << "\n";
    }

    // push_backで追加
    v.push_back(4);
    cout << "Adding...\n";

    // 確認
    for (int i=0; i < v.size(); i++) {
    cout << v[i] << "\n";
    }
}