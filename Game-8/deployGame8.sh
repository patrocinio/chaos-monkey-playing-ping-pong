NAME=ping-player
NAMESPACE=ping-pong

HELM_OPTIONS=
#HELM_OPTIONS=

echo Deleting $NAME
helm delete $NAME $HELM_OPTIONS

echo Deploying $NAME
helm install $NAME ./helm/ping-player --namespace $NAMESPACE $HELM_OPTIONS
