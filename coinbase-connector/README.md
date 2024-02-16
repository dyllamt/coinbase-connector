# coinbase-connector

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

Forwarding service from coinbase to kafka.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| connector.appName | string | `"coinbase-connector"` | app name linking deployment and service |
| connector.deploymentName | string | `"coinbase-connector-deployment"` | name of deployment in k8s |
| connector.image | string | `"coinbase-connector:latest"` | deployment image |
| connector.imagePullPolicy | string | `"Never"` | image pull policy |
| connector.replicas | int | `1` | replicas for deployment |
| connector.serviceName | string | `"coinbase-connector-service"` | name of service in k8s |
| kafka.address | string | `"coinbase-cluster-kafka-bootstrap.dev.svc.cluster.local:9092"` | address of the kafka cluster |
| kafka.clusterName | string | `"coinbase-cluster"` | name of the kafka cluster |
| kafka.clusterNamespace | string | `"dev"` | namespace where kafka is deployed |
| kafka.topic | string | `"ticker"` | the topic to forward data to |

