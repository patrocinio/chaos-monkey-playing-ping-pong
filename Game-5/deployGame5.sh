oc apply -f cluster-image-policy.yaml
oc adm policy add-scc-to-user anyuid -z default

./deployChart.sh cache

echo Waiting 10 seconds
sleep 10

./deployChart.sh ping-player
