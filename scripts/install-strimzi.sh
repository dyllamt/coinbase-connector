#!/bin/bash

# namespace for dev
kubectl create namespace dev

# strimzi operator
helm repo add strimzi http://strimzi.io/charts/
helm repo update
helm install strimzi-operator strimzi/strimzi-kafka-operator --namespace dev --wait