#-uを指定しない場合はroot権限で実行するが、-uでユーザーidを指定して実行が可能
#docker run -it -u $(id -u):$(id -g) -v C:/Users/nakam/Desktop/docker//created_in_run:/created_in_run <ID> bash

#$(id -u) が linuxで id-uとした結果の意味だが、windowsだと動かないので、git-bashでid-u, id-gを確認した結果を入れて以下のようにした。
#docker run -it -u 197609:197609 -v C:/Users/nakam/Desktop/docker//created_in_run:/created_in_run <ID> bash

#ls -laでファイルの権限を確認可能
#docker_fileで作成するcreated_in_Dockerfileはroot権限で作られているので、197609からtouch testなどでファイルを作ることはできない。
#docker run で作成したcreated_in_runの中にはtouch testでファイルを作成することが可能。


FROM ubuntu:16.04
RUN mkdir created_in_Dockerfile