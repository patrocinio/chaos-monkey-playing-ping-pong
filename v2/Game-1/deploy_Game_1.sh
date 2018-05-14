NAME=ping-pong

echo Deleting $NAME
helm delete $NAME --purge --tls

echo Deploying $NAME
helm install --name $NAME ./ping-pong --tls