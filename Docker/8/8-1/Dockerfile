# sudo: linuxでルート権限以外のユーザーがコメントを実行する際に使用
# wget: httpを使ってインターネットからプログラムをとってくる
# vim : Editor
From ubuntu:16.04
# apt-getを使う前にはupdateをしておかないと、古いファイルをとってきたりする
RUN apt-get update && apt-get install -y\
    sudo \
    wget \
    vim 

# rootに置くと他のユーザーがアクセスしにくいので、/optに置く
WORKDIR /opt 

#Anacondaをインストーラを取得
RUN wget https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh

