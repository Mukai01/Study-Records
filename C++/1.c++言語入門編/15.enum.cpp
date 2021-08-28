#include <iostream>
using std::cout;


int main() {
    // 固定値を持つenum Colorを作成する
    enum class Color {white, black, blue, red};

    // カラー変数を作成し、ブルーに設定
    Color my_color = Color::blue;

    if (my_color == Color::red) {
        cout << "The color or my car is red" << "\n";
    } else {
        cout << "The color of my car is not red" << "\n";
    }

    // スイッチ文と組み合わせることも可能
    enum class Direction {kUp, kDown, kLeft, kRight};

    Direction a = Direction::kUp;

    switch (a) {
        case Direction::kUp : cout << "Going up!\n";
            break;
        case Direction::kDown : cout << "Going down!\n";
            break;
        case Direction::kLeft : cout << "Going left!\n";
            break;
        case Direction::kRight : cout << "Going right!\n";
            break;
    }
}