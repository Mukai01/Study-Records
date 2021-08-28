// ヘッダファイルの中で変数、関数、クラスを定義すると他のファイルから使用可能

// ifndef: Header_Example_hがそのファイルですでに定義されていないかをチェック
// define: もし定義されていなければ、defineで定義される
// これらはプリプロセッサと呼ばれる、コンパイル前に実行されるコマンド
// もしすでに定義されていたら、コンパイルされない（条件コンパイル）

#ifndef HEADER_EXAMPLE_H
#define HEADER_EXAMPLE_H

void OuterFunction(int);
void InnerFunction(int);

#endif