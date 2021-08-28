// ファイルストリーミングクラスを提供するヘッダファイルfstreamを使う
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std :: ifstream my_file;
    my_file.open("files/board");
    if (my_file) {
        std :: cout << "The file stream has been created! \n";
        std :: string line;
        // getlineでファイルの行を文字列に書き込む
        while (getline(my_file, line)) {
            std::cout << line << "\n";
        }
    }
}