<div align="center">

<h1>coinbase-producer</h1>
<p>Kafka producer for coinbase feeds.</p>

![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
[![](https://img.shields.io/badge/docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://github.com/dyllamt/coinbase-producer/pkgs/container/coinbase-producer)
[![](https://img.shields.io/badge/helm-0F1689?style=for-the-badge&logo=Helm&labelColor=0F1689)](https://github.com/dyllamt/coinbase-producer/tree/gh-pages/)

</div>


## Logging

#### Info
- subscription messages sent to coinbase.
- messages consumed from coinbase.
#### Warnings
- coinbase reconnection errors.

## Local Testing

- `make install` install python dependencies.
- `make test-format` tests formating and performs static type checking.
- `make test-unit` tests live message consumption to a mock kafka stream.
- `make test-integration` tests helm deployment with kafka broker.

## CI/CD
- `pull request` format, unit, and integration tests.
- `merge to main` docker and helm release (if [version](https://github.com/dyllamt/coinbase-producer/blob/main/VERSION) bumped).

## Deployment

Message deduplication should be implemented if the producer is replicated.