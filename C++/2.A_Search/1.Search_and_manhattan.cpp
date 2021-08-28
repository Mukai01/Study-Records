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
using std::abs;

enum class State {kEmpty, kObstacle};

vector<State> ParseLine(string line) {
    istringstream sline(line);
    int n;
    char c;
    vector<State> row;
    while (sline >> n >> c && c == ',') {
      if (n == 0) {
        row.push_back(State::kEmpty);
      } else {
        row.push_back(State::kObstacle);
      }
    }
    return row;
}


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

string CellString(State cell) {
  switch(cell) {
    case State::kObstacle: return "⛰️   ";
    default: return "0   "; 
  }
}


void PrintBoard(const vector<vector<State>> board) {
  for (int i = 0; i < board.size(); i++) {
    for (int j = 0; j < board[i].size(); j++) {
      cout << CellString(board[i][j]);
    }
    cout << "\n";
  }
}

// Search関数を作成
// まずは、引数を受け取って、NoPathfoundを返す
vector<vector<State>> Search(vector<vector<State>> grid, int init[2],int goal[2]) {
    cout << "No path found!" << "\n";
    return vector<vector<State>> {};
}

// manhattan distanceを計算する
int Heuristic(int x1, int y1, int x2, int y2) {
  return abs(x2 - x1) + abs(y2 - y1);
}

// 実行
int main() {
  //配列を作成   
  int init[2]{0, 0};
  int goal[2]{4, 5};
  
  auto board = ReadBoardFile("Root/board.txt");
  // Searchを試行
  auto solution = Search(board, init, goal);
  // マンハッタン距離を計算
  int dist = Heuristic(0,0,3,3);
  cout << "distance:" << dist << "\n";

  PrintBoard(solution);
}