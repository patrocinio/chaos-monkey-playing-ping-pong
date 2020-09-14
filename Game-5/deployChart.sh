NAME=$1
CHART=./helm/$1
NAMESPACE=ping-pong

HELM_OPTIONS=
#HELM_OPTIONS=

echo Deleting $NAME
helm delete $NAME $HELM_OPTIONS

echo Waiting 4 seconds...
sleep 4

echo Deploying $NAME
helm install $NAME $CHART --namespace $NAMESPACE $HELM_OPTIONS
