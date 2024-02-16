# coinbase-kafka

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

Strimzi: Apache Kafka running on Kubernetes

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cluster.kafka.replicas | int | `1` | number of broker replicas |
| cluster.storage | string | `"ephemeral"` | storage class for broker logs |
| cluster.zookeeper.replicas | int | `1` | number of zookeper replicas |
| topics | list | `["ticker"]` | topics on the cluster |

