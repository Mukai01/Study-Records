#include "header_example.h" // この1文がないと関数の順序でエラーが出てしまう

#include <iostream>
#include <vector>
using std::vector;
using std::cout;

void OuterFunction(int i) {
    InnerFunction(i);
    }

void InnerFunction(int i) {
     std::cout << i << "\n";
    }

int main() {
    int a = 5;
    OuterFunction(a);
    }
