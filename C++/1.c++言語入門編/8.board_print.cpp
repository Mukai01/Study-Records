// これまでに並んだことを使って、ボードをprintする関数を作る
#include <iostream>
#include <vector>
using std::cout;
using std::vector;

void PrintBoard(const vector<vector<int>> board) {
//2重forループ 
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            cout << board[i][j];
        }
    cout << "\n";
  }
}

// 実行
int main() {
  vector<vector<int>> board{{0, 1, 0, 0, 0, 0},
                            {0, 1, 0, 0, 0, 0},
                            {0, 1, 0, 0, 0, 0},
                            {0, 1, 0, 0, 0, 0},
                            {0, 0, 0, 0, 1, 0}};
  PrintBoard(board);
}