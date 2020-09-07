![Sawtooth=BGX](bgx/images/logo-bgx.png)

Hyperledger DGT SDK
-------------

Hyperledger Sawtooth-BGX is an enterprise solution for building, deploying, and
running distributed ledgers (also called blockchains). It provides an extremely
modular and flexible platform for implementing transaction-based updates to
shared state between untrusted parties coordinated by consensus algorithms.

.
# install befor start validator
# git clone http://gitlab.ntrlab.ru:83/ntrlab/bgx.git
# sudo apt install docker
# sudo apt install docker.io
# sudo apt install docker-compose
# sudo usermod -aG docker dgt
# sudo apt-get install curl
# sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose
# composer 
# sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#start TP 
bash upTproc.sh 1 1
#stop TO 
bash downTproc.sh 1 1

#For running shell-dgt run next bash cmd .
$ docker exec -it shell-dgt-c1-1 bash

# start REST-API 
bash upRest.sh 1 1  
# stop REST-API
bash downRest.sh 1 1

# for admin console
#bgx dag show val --url http://bgx-api-2:8009;echo ---;bgx dag show nest --url http://bgx-api-c1-2:8009 -Fjson
#bgx dag show integrity --url http://bgx-api-c1-1:8008;bgx dag show integrity --url http://bgx-api-c1-2:8009
#bgx block list --url http://bgx-api-c1-1:8008;bgx block list --url http://bgx-api-c1-2:8009
#



# start node 1 in cluster 1
bash upCluster.sh -G 1 1 
# stop node 1 in cluster 1
bash downCluster.sh -G 1 1


