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

# Anacondaをインストーラを取得
# 以下を10-1で調査した方法で記述する
# rm -f で強制的に削除
RUN wget https://repo.continuum.io/archive/Anaconda3-2020.07-Linux-x86_64.sh && \
    sh Anaconda3-2020.07-Linux-x86_64.sh  -b -p /opt/anaconda3 && \
    rm -f Anaconda3-2020.07-Linux-x86_64.sh

# PATHに追加
ENV PATH /opt/anaconda3/bin:$PATH

# pipをアップグレード
RUN pip install --upgrade pip

# ディレクトリをルートに戻す
WORKDIR /

# コマンドとオプションを指定
# --ip : 0.0.0.0がローカルホストの意味⇒ローカルホストで動くようになる
# --allow-root : ルートで動かすことを許可s
# --LabApp.token : 自分のPCでセキュリティを考えなくてよいので、今回は無しで指定
CMD ["jupyter","lab","--ip=0.0.0.0","--allow-root","--LabApp.token=''"]