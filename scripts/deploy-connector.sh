#!/bin/bash

# Install connector chart 
helm install coinbase-connector ../kubernetes/connector/ -f ../kubernetes/connector/values.yaml --namespace dev --wait
