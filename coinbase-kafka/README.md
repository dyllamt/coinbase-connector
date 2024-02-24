# coinbase-kafka

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square)

Kafka broker chart for coinbase feeds.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cluster.broker.replicas | int | `1` | number of broker replicas |
| cluster.name | string | `"coinbase-kafka"` | name of strimzi kafka crd |
| cluster.storage | string | `"ephemeral"` | storage class for broker logs |
| cluster.zookeeper.replicas | int | `1` | number of zookeper replicas |
| topics | list | `["ticker"]` | published topics |

