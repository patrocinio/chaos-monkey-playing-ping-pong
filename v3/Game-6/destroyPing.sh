echo Getting Ping Pods
PID=$(kubectl get pod -l app=ping --no-headers=true | awk '{print $1}' | head -1)

echo Deleting Pod $PID
kubectl delete pod $PID

