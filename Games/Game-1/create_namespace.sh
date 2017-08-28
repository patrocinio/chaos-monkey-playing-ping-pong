CONTEXT=minikube

kubectl create namespace ping-pong
kubectl config set-context $CONTEXT --user=user --namespace=ping-pong
