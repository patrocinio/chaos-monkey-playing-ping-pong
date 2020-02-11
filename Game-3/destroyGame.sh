NAME=ping-pong
NAMESPACE=ping-pong

HELM_OPTIONS=--tiller-namespace=tiller


echo Deleting $NAME
helm delete $NAME --purge $HELM_OPTIONS
