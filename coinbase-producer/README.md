# coinbase-producer

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square)

Kafka producer for coinbase feeds.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| kafka.address | string | `"coinbase-kafka-kafka-bootstrap.dev.svc.cluster.local:9092"` | address of the kafka cluster |
| kafka.clusterName | string | `"coinbase-kafka"` | name of the kafka cluster |
| kafka.clusterNamespace | string | `"dev"` | namespace where kafka is deployed |
| kafka.topic | string | `"ticker"` | the topic to forward data to |
| producer.appName | string | `"coinbase-producer"` | app name linking deployment and service |
| producer.deploymentName | string | `"coinbase-producer-deployment"` | name of deployment in k8s |
| producer.image | string | `"coinbase-producer:latest"` | deployment image |
| producer.imagePullPolicy | string | `"IfNotPresent"` | image pull policy |
| producer.replicas | int | `1` | replicas for deployment |
| producer.serviceName | string | `"coinbase-producer-service"` | name of service in k8s |

