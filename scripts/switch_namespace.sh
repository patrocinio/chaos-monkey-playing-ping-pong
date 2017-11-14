CONTEXT=mycluster.icp-context
USER=mycluster.icp-user

kubectl config set-context $CONTEXT --user=$USER --namespace=ping-pong
kubectl config get-contexts

