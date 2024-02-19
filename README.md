# coinbase-connector
Connector between coinbase websocket feeds and kafka.

# Contents

The application impliments an async webserver that subscribes to coinbase websocket feeds and forwards the messages to kafka. It is recommended that you deploy it in a replica set.

## Docker

There is a docker image of the application published [here](https://github.com/dyllamt/coinbase-connector/pkgs/container/coinbase-connector).

## Helm

There is a packaged chart published [here](https://github.com/dyllamt/coinbase-connector/tree/gh-pages). A starter chart for kafka is also included.

# Developer Notes

## CI/CD
- on pull requests: format, unit, and integration tests.
- merge into main: docker and helm release (if [version](https://github.com/dyllamt/coinbase-connector/blob/main/VERSION) bumped).

## Local Testing

- `make install` install python dependencies.
- `make test-format` tests formating and performs static type checking.
- `make test-unit` tests live message consumption to a mock kafka stream.
- `make test-integration` tests helm deployment with kafka broker.

## Logging

#### Info
- subscription messages sent to coinbase.
- messages consumed from coinbase.

#### Warnings
- coinbase reconnection errors.

## Replicas

If multiple replicas are deployed, kafka consumers should implement deduplication logic.