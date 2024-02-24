#!/bin/bash

# namespace for dev
NAMESPACE="dev"
kubectl create namespace $NAMESPACE

# strimzi operator
helm repo add strimzi http://strimzi.io/charts/
helm repo update
helm install strimzi-operator strimzi/strimzi-kafka-operator --namespace $NAMESPACE --wait

# kafka cluster
helm install coinbase-kafka ../charts/coinbase-kafka/ -f ../charts/coinbase-kafka/values.yaml --namespace $NAMESPACE --wait

# coinbase connector
helm install coinbase-producer ../charts/coinbase-producer/ -f ../charts/coinbase-producer/values.yaml --namespace $NAMESPACE --wait
