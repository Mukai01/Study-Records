#include <iostream>
#include <sstream>
#include <string>

using std::istringstream;
using std::string;
using std::cout;

int main(){
    // 文字列を指定
    string a = "12a 2 3";

    // istringstreamオブジェクトを作成
    istringstream my_stream(a);

    int n;
    // スペースもしくは抽出に失敗するまで読み込む
    my_stream >> n;
    cout << n << "\n";

    // 任意の1文字を格納できるcharを使用する 
    string b = "12,3,4a";
    istringstream my_stream2(b);
    char c;

    // my_streamは失敗したらfalseになるので、whileに使用可能
    // n,cに格納出来たらTrueとなる
    while (my_stream2 >> n >> c){
        cout << "success:" << n << " " << c << "\n";
    }
    cout << "failed\n" ;
}