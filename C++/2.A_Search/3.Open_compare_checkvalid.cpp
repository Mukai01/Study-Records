#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>  // for sort
using std::cout;
using std::ifstream;
using std::istringstream;
using std::string;
using std::vector;
using std::abs;
using std::sort;

// チェック済みを表すkClosedを追加
enum class State {kEmpty, kObstacle, kClosed, kPath};

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

// manhattan distanceを計算する
int Heuristic(int x1, int y1, int x2, int y2) {
  return abs(x2 - x1) + abs(y2 - y1);
}

// Openvectorに追加し、gridをkclosedに変更
void AddToOpen(int x, int y, int g, int h, vector<vector<int>> &openlist, vector<vector<State>> &grid) {
  openlist.push_back(vector<int>{x, y, g, h});
  grid[x][y] = State::kClosed;
}

// 比較関数を作成
// constで宣言すると、その関数の中では書き変え不可能
bool Compare(const vector<int> a, const vector <int> b) {
  // f = g + h
  int f1 = a[2] + a[3];
  int f2 = b[2] + b[3];
  return f1 > f2;
}

// 2次元ベクトルを降順に並べ替える関数
// まだ理解できなくていい
void CellSort(vector<vector<int>> *v) {
  sort(v->begin(),v->end(),Compare);
}

//グリッド上にあるか、障害物がないかを確認する関数 
bool CheckValidCell(int x, int y, vector<vector<State>> &grid) {
  bool on_grid_x = (x >= 0 && x < grid.size()); 
  bool on_grid_y = (y >= 0 && y < grid[0].size());
  if (on_grid_x && on_grid_y)
    //空であればTrueを返す
    return grid[x][y] == State::kEmpty;
  return false;
}

// Search関数を作成
vector<vector<State>> Search(vector<vector<State>> grid, int init[2],int goal[2]) {
  // openvectorを作成
  vector<vector<int>> open {};

  // 初期値の設定
  int x = init[0];
  int y = init[1];
  int g = 0;
  int h = Heuristic(x, y, goal[0], goal[1]);

  // Addtoopenを実行
  AddToOpen(x, y, g, h, open, grid);

  while (open.size() > 0) {
    // 次のノードを取得
    CellSort(&open);
    // openの最後の要素を格納
    auto current = open.back();
    // 最後の要素を削除
    open.pop_back();
    // x,yを更新
    x = current[0];
    y = current[1];
    // kPathに変更
    grid[x][y] = State::kPath;

    // 完了判定
    if (x == goal[0] && y == goal[1]) {
      return grid;
    }

    // 完了じゃない場合
    // ExpandNeighbors
  }
  cout << "No path found!" << "\n";
  return vector<vector<State>> {};
}


// 実行
int main() {
  //配列を作成   
  int init[2]{0, 0};
  int goal[2]{4, 5};
  
  auto board = ReadBoardFile("files/board.txt");
  // Searchを試行
  auto solution = Search(board, init, goal);
  // Compareを試行
  auto compare_result = Compare(vector<int> {0,0,4,2}, vector<int> {0,0,2,3});
  cout << "Compare:" << compare_result << "\n";
  // CheckValidCellを試行
  auto checkvalid = CheckValidCell(0,2,board);
  cout << "valid:" << checkvalid << "\n";
  PrintBoard(board);
}