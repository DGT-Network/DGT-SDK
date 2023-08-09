![DGT](images/logo-dgt.png)

Hyperledger DGT SDK
-------------

DGT is an enterprise solution for building, deploying, and
running distributed ledgers (also called blockchains). It provides an extremely
modular and flexible platform for implementing transaction-based updates to
shared state between untrusted parties coordinated by consensus algorithms.

.
# install DGT node

#start devel 

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


