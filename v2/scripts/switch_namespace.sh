CONTEXT=mycluster.icp-context
USER=admin

kubectl config set-context $CONTEXT --user=$USER --namespace=ping-pong
kubectl config get-contexts

