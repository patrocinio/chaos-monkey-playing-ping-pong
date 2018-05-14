NAME=ping-pong

helm delete $NAME --purge --tls


cd ping-pong
helm dependency update

cd ..
helm install --name $NAME ./ping-pong --tls