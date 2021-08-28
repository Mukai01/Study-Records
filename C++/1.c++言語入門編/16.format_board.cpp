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

enum class State {kEmpty, kObstacle};

// vector<State>に変更
vector<State> ParseLine(string line) {
    istringstream sline(line);
    int n;
    char c;
    // vector<State>に変更
    vector<State> row;
    while (sline >> n >> c && c == ',') {
        // if文を追加
        if (n==0) {
            row.push_back(State::kEmpty);
        } else {
            row.push_back(State::kObstacle);
        }
    }
    return row;
}

// vector<state>に変更
vector<vector<State>> ReadBoardFile(string path) {
    ifstream myfile (path);
    vector<vector<State>> board{};
    if (myfile) {
        string line;
        while (getline(myfile, line)) {
            vector<State> row = ParseLine(line);
            board.push_back(row);
        }
    }
    return board;
}

// State⇒文字に変換
string CellString(State cell) {
    switch(cell) {
        case State::kObstacle: return "⛰️   ";
        default: return "0   "; 
    }
}

void PrintBoard(const vector<vector<State>> board) {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            //printする前にCellStringを適用 
            cout << CellString(board[i][j]);
        }
        cout << "\n";
    }
}

// 実行
int main() {
  auto board = ReadBoardFile("files/board.txt");
  PrintBoard(board);
}