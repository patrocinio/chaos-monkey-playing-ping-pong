echo Deleting clean_cache job
kubectl delete job clean-cache

echo Deploying clean cache
kubectl create -f clean_cache/deploy/clean_cache_job.yaml