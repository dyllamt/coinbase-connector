import asyncio
import json

import coinbase.main as main


def test_connect_and_serve_messages(kafka_producer):
    print("cool")

    # run streaming loop for 10 seconds
    try:
        asyncio.run(
            asyncio.wait_for(
                main.connect_and_serve_messages(main.default_coinbase_address, producer=kafka_producer, topic=""),
                timeout=5,
            )
        )
    except asyncio.TimeoutError:
        pass

    # make sure we saw some messages
    assert len(kafka_producer.messages) > 3

    # make sure they are valid json
    for message in kafka_producer.messages:
        payload = json.loads(message)
        assert isinstance(json.dumps(payload), str)

    # make sure they have uniform schema
    keys = [set(json.loads(i).keys()) for i in kafka_producer.messages]
    for ks in keys:
        assert keys[0] == ks
