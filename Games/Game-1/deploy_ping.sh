echo Deleting ping  Pod
kubectl delete pod ping

while [ ! -z `kubectl get po | grep ping` ]
do
	sleep 1
done

echo Deploying ping Pod
kubectl create -f ping_pong/src/ping_pod.yaml