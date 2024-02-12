# coinbase-connector
Connector between coinbase websocket feeds and kafka.


# Developer Notes

## Testing

- `make install` install python dependencies.
- `make test-format` tests formating and performs static type checking.
- `make test-unit` tests live message consumption to a mock kafka stream.
- `make test-integration` tests helm deployment with kafka broker.

## Deployment

#### Environment variables

- `kafka_address` (required) Url and port for kafka service.
- `kafka_topic` (required) Name of the topic to forward messages to.
- `coinbase_address` (optional) Url for coinbase websocket feeds.

## Logging

#### Info
- subscription messages sent to coinbase
- messages consumed from coinbase

#### Warnings
- coinbase reconnection errors

## Replicas

If multiple replicas are deployed, kafka consumers should implement deduplication logic.