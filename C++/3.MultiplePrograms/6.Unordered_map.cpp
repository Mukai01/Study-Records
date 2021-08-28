// マップ（ハッシュテーブル）はkey.valueペアを使用してデータを格納する
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using std::vector;
using std::cout;
using std::unordered_map;
using std::string;

int main() {
    string key = "word";
    string def_1 = "a unit of language, consisting of one or more spoken sounds or their written representation, that functions as a principal carrier of meaning";
    string def_2 = "speech or talk: to express one's emotion in words";
    string def_3 = "a short talk or conversation: 'Marston, I'd like a word with you.'";
    string def_4 = "an expression or utterance: a word of warning";
    unordered_map <string, vector<string>> my_dictionary;

    // .findは見つかればiteratorを返すが、見つからないとunordered_map::end()型を返す
    // まだ辞書は空なので、見つからない
    if (my_dictionary.find(key) == my_dictionary.end()) {
        cout << "The key 'word' is not in the dictionary." << "\n";
        cout << "Inserting a key-value pair into the dictionary." << "\n\n";
    }

    // 辞書に登録
    my_dictionary[key] = vector<string> {def_1, def_2, def_3, def_4};
    // 結果の確認
    cout << my_dictionary[key][0] << "\n";

    // 以下のように辞書を作成することも可能
    unordered_map<int, std::string> mymap {
        {5, "a"},
        {6, "b"},
        {7, "c"} 
    };
    // 結果の確認
    cout << mymap[6];
}