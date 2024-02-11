#!/bin/bash

# Install connector chart 
helm install coinbase-connector ../charts/connector/ -f ../charts/connector/values.yaml --namespace dev --wait
