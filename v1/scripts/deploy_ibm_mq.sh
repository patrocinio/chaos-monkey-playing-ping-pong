echo Deleting IBM queue chart
helm delete --purge ibm-mq

echo Adding repo
helm repo add ibm https://raw.githubusercontent.com/IBM/charts/master/repo/stable/

echo Deploying IBM queue chart
helm install --name ibm-mq ibm/ibm-mqadvanced-server-dev --set license=accept,persistence.enabled=false,queueManager.dev.appPassword=ping_pong
