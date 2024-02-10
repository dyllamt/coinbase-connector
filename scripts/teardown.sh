helm uninstall -n dev coinbase-connector --wait
helm uninstall -n dev kafka-cluster --wait
helm uninstall -n dev strimzi-operator --wait