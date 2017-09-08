#CONTEXT=minikube
#USER=minikube

CONTEXT=cfc
USER=cfcadmin

kubectl create namespace ping-pong
kubectl config set-context $CONTEXT --user=$USER --namespace=ping-pong
