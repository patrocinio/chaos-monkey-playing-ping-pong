#CONTEXT=minikube
#USER=minikube

#CONTEXT=cfc
#USER=user

CONTEXT=mycluster.icp-context
USER=admin

kubectl create namespace ping-pong
kubectl config set-context $CONTEXT --user=$USER --namespace=ping-pong
kubectl config get-contexts

