# coinbase-kafka

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square)

Simple kafka deployment for coinbase data.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cluster.kafka.replicas | int | `1` | number of broker replicas |
| cluster.storage | string | `"ephemeral"` | storage class for broker logs |
| cluster.zookeeper.replicas | int | `1` | number of zookeper replicas |
| topics | list | `["ticker"]` | topics on the cluster |

