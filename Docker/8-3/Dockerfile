#cd 8-3
#docker build .
#docker images でIDを確認
#docker run -it <ID> bash
#env で環境変数を表示可能
#ls sample_folder　でファイルができていることを確認可能

FROM ubuntu:16.04

#環境変数を設定
ENV key1 value
ENV key2=value

#無ければフォルダを作成して、以降そこで作業する
WORKDIR /sample_folder
RUN touch sample_file
#最後に戻す
WORKDIR /

#以下のように書いても同じことが可能
RUN mkdir sample_folder2 && \
    cd sample_folder2 && \
    touch sample_file2