import asyncio
import json
import logging
import sys

import kafka
import websockets

# logging configuration

logger = logging.getLogger("coinbase-producer")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


# kafka producer configuration


def kafka_producer(server_address: str) -> kafka.KafkaProducer:
    return kafka.KafkaProducer(
        bootstrap_servers=[server_address],
        value_serializer=lambda v: v.encode("utf-8"),
    )


async def publish_message_to_kafka(producer: kafka.KafkaProducer, topic: str, message: str) -> None:
    logger.info(f"{message}")
    producer.send(topic, message)


# coinbase consumption logic

default_coinbase_address = "wss://ws-feed.exchange.coinbase.com"

coinbase_subscription_message = {"type": "subscribe", "product_ids": ["ETH-USD", "BTC-USD"], "channels": ["ticker"]}


async def subscribe_to_feeds(websocket: websockets.WebSocketClientProtocol):  # type: ignore
    await websocket.send(json.dumps(coinbase_subscription_message))


async def message_handler(
    websocket: websockets.WebSocketClientProtocol, producer: kafka.KafkaProducer, topic: str  # type: ignore
):
    async for message in websocket:
        await publish_message_to_kafka(producer, topic, message)  # type: ignore


async def connect_and_serve_messages(coinbase_address: str, producer: kafka.KafkaProducer, topic: str):
    async with websockets.connect(coinbase_address) as websocket:  # type: ignore
        await subscribe_to_feeds(websocket)
        subscription = await websocket.recv()  # skip the first message, which is the subscription message
        logger.info(f"{subscription}")  # type: ignore
        await message_handler(websocket, producer, topic)


# client reads from coinbase feed and publishes to kafka


async def main(coinbase_address: str, kafka_address: str, kafka_topic: str):
    """Kafka producer for coinbase feeds.

    Reconnect error handling and logging is implemented.

    Parameters
    ----------
    coinbase_address : str
        Url for coinbase websocket feeds.
    kafka_address : str
        Url and port for kafka service.
    kafka_topic : str
        Name of the topic to forward messages to.
    """
    producer = kafka_producer(server_address=kafka_address)

    while True:
        try:
            await connect_and_serve_messages(coinbase_address, producer, kafka_topic)
        except websockets.ConnectionClosed:  # type: ignore
            logger.warning("Connection closed: reconnecting after 5 seconds...")
            await asyncio.sleep(5)


if __name__ == "__main__":
    import os

    COINBASE_ADDRESS = os.environ.get("COINBASE_ADDRESS", default_coinbase_address)
    KAFKA_ADDRESS = os.environ.get("KAFKA_ADDRESS", "")
    KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "")

    asyncio.run(main(COINBASE_ADDRESS, KAFKA_ADDRESS, KAFKA_TOPIC))
