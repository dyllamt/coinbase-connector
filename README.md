# coinbase-connector
Connector between coinbase websocket feeds and kafka.

# Contents

There are two packaged charts developed in this project. You can find docs on the latest versions here:
https://github.com/dyllamt/coinbase-connector/tree/gh-pages.

# Developer Notes

## Local Testing

- `make install` install python dependencies.
- `make test-format` tests formating and performs static type checking.
- `make test-unit` tests live message consumption to a mock kafka stream.
- `make test-integration` tests helm deployment with kafka broker.

## Logging

#### Info
- subscription messages sent to coinbase
- messages consumed from coinbase

#### Warnings
- coinbase reconnection errors

## Replicas

If multiple replicas are deployed, kafka consumers should implement deduplication logic.