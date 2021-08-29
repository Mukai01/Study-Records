# docker build . でdockerimageができる
# docker run -it <ID> bash　でコンテナが作成される
# ls /new_dir を確認するとsomethingがあることが確認できる
# ls sample_folder でhelloがあることが確認できる

FROM ubuntu:16.04
RUN mkdir /new_dir
# somethingファイルをnew_dir直下にコピー
COPY something /new_dir/
# 解凍して、ルート直下に配置
ADD compressed.tar /
