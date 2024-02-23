# coinbase-producer
Kafka producer for coinbase feeds.

#### Replicas

If replicas are deployed, message deduplication should be implemented in downstream components.

# Packages

[Producer image](https://github.com/dyllamt/coinbase-producer/pkgs/container/coinbase-producer)
[Producer chart](https://github.com/dyllamt/coinbase-producer/tree/gh-pages/coinbase-producer).
[Kafka chart](https://github.com/dyllamt/coinbase-producer/tree/gh-pages/coinbase-kafka)

# Developer Notes

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
- `pull request`: format, unit, and integration tests.
- `merge to main`: docker and helm release (if [version](https://github.com/dyllamt/coinbase-producer/blob/main/VERSION) bumped).
