// mainでやったことをスケーリングする
#include <iostream>
#include <string>
#include <vector>
#include "car.h"
using std::string;
using std::cout;
using std::vector;

int main() {
    // 車へのポインタの空のベクトルと車へのヌルポインタを作成する。
    vector<Car*> car_vect;
    Car* cp = nullptr; //空のポインタはnullptrと表記する

    // 車の色のベクトル:
    vector<string> colors {"red", "blue", "green"};

    // 色の異なる100台の車を作成し、それらの車それぞれへのポインタをベクトルに押し込む。
    for (int i=0; i < 100; i++) {;
        // newは新しいCarのために、"ヒープ"上にメモリを割り当てる
        cp = new Car(colors[i%3], i+1);
        car_vect.push_back(cp);
    }

    // 各車を1つずつ前に進める。
    // -> 演算子はデリファレンスして、メソッドを使う　ということ
    // (*cp).IncrementDistance() でも同じ結果となる

    // car_vectの中には、作成したCarインスタンスのポインタ達が入っている
    for (Car* cp: car_vect) {
        cp->IncrementDistance();
    }

    // 各車のデータを印刷する。
    for (Car* cp: car_vect) {
        cp->PrintCarData();
    }
}