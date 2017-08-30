destroy_ping.sh

kubectl delete rs ping
kubectl delete rs pong
kubectl delete rs commentator

kubectl delete job throw-ball

helm delete --purge queue
