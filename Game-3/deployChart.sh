NAME=$1
CHART=./helm/$1
NAMESPACE=ping-pong

HELM_OPTIONS=--tiller-namespace=tiller
#HELM_OPTIONS=

echo Deleting $NAME
helm delete $NAME --purge $HELM_OPTIONS

echo Waiting 30 seconds...
sleep 30

echo Deploying $NAME
helm install --name $NAME $CHART --namespace $NAMESPACE $HELM_OPTIONS
