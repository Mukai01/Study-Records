#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using std::cout;
using std::ifstream;
using std::istringstream;
using std::string;
using std::vector;

//文字列　⇒ vector変換関数
vector<int> ParseLine(string line) {
    istringstream my_stream(line);
    int n;
    char c;
    vector <int> row;

    while (my_stream >> n >> c){
        cout << "success:" << n << " " << c << "\n";
        row.push_back(n);
    }
    cout << "Comp\n" ;
    return row;
}

// ファイル読み込み ⇒ 文字列変換関数
vector<vector<int>> ReadBoardFile(string path) {
    ifstream myfile (path);
    cout << "Start reading...";

    // boardの箱を作成
    vector<vector<int>> board{};
    if (myfile) {
        string line;
        while (getline(myfile, line)) {
            cout << line << "\n";
            //上記の関数を呼び出す
            vector<int> row = ParseLine(line);
            // boardに格納
            board.push_back(row);   
    }
  }
  return board;
}

// boardを印刷する関数
void PrintBoard(const vector<vector<int>> board) {
  for (int i = 0; i < board.size(); i++) {
    for (int j = 0; j < board[i].size(); j++) {
      cout << board[i][j];
    }
    cout << "\n";
  }
}

// 実行
int main() {
  auto board = ReadBoardFile("files/board.txt");
  PrintBoard(board);
}