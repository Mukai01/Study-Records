#include <iostream>
#include <string>
using std::cout;
using std::string;

// $iとすることで、参照渡しとなり、元データが変更される
int MultiplyByTwo(int &i) {
    i = 2*i;
    return i;
}

void DoubleString(string &value) {
    value = value + " " + value;
}

int main() {
    int a = 1;
    int b = MultiplyByTwo(a);
    cout << "a=" << a << "\n";
    cout << "b=" << b << "\n"; 

    string s = "hello";
    DoubleString(s);
    cout << s << "\n";
}