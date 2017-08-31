echo Deleting commentator Replica Set
kubectl delete rs commentator

echo Deploying commentator Replica Set
kubectl create -f commentator/deploy/commentator_rset.yaml