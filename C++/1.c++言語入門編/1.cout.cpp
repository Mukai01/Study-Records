// c++の入出力オブジェクトを使用するのに必要
// include:コードがコンパイルされる前に実行されるコマンド
// 　　　　 iostreamというファイルを検索して、その内容を貼り付ける
// iostream:入出力オブジェクトの宣言が含まれる
#include <iostream>

// 名前空間stdは標準ライブラリで使用される名前空間
// usingは std::cout をプログラムのグローバルスコープに追加する
// 　⇒これにより、std::coutと書かなくてもcoutを使える
// coutは出力ストリーム
using std::cout;

int main() {
    cout << "Hello";
}
