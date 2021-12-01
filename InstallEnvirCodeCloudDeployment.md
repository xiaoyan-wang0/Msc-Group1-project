### Installation environment code for cloud deployment

## git

sudo apt install git

## Docker

sudo apt update


sudo apt install apt-transport-https ca-certificates curl software-properties-common


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

apt-cache policy docker-ce

sudo apt install docker-ce

sudo systemctl status docker


sudo apt install net-tools

ifconfig

sudo docker swarm init --listen-addr IP

 sudo docker node ls

 sudo docker service create --name tensorflow --replicas 1 -p 850
 0 :8500 -p 8501:8501 \--mount type=bind,source=/home/ubuntu/models/week6_model,target=/mod
 els/mymodel \--mount type=bind,source=/home/ubuntu/models/Test_model_Bert2,target=/models/
 mymodel2  \--mount type=bind,source=/home/ubuntu/models/model.config,target=/models/model.
 config \-t tensorflow/serving --model_config_file=models/model.config tensorflow:latest

 curl IP/v1/models/mymodel

## Frontend


sudo apt-get install nginx

sudo apt install uwsgi

## Backend

sudo apt install mysql-server

sudo apt install python3-pip

sudo apt-get install mysql-client

sudo apt-get install libmysqlclient-devs

sudo pip install -r requirement.txt

#or

pip install "Flask==1.1.4"

pip install mumpy

pip install pandas

pip install ipywidgets

pip install tweepy

pip install flask_cors

pip install lxml

pip install bs4

pip install jsonpath

pip install flask_debugtoolbar

pip install tmdbv3api

pip install uwsgi

pip install Flask-SQLAlchemy

pip install tensorflow --no-cache-dir

pip install requests-futures

pip install seaborn

pip install sklearn
