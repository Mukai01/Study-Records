# docker build . でdockerimageができる
# docker run <ID>　でコンテナが作成される

#FROMはDocker imageのベースを指定する
FROM ubuntu:16.04

#Runはimage layerを作る
#apt-get install -y ですべてyesでインストールする
#RUNをするたびにlayerが作られるので、 &&でまとめた方がよい
RUN apt-get update
RUN apt-get install -y \
    curl \
    nginx

# RUNはLayerを作るが、CMDは作らない
# CMDはrunした場合に実行される
CMD ["ls"]