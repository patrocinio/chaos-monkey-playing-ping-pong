export TILLER_NAMESPACE=tiller

oc adm policy add-cluster-role-to-user cluster-admin "system:serviceaccount:${TILLER_NAMESPACE}:tiller"
