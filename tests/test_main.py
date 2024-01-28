import asyncio
import json

import coinbase.main as main


def test_connect_and_serve(kafka_producer):

    # run streaming loop for 10 seconds
    try:
        asyncio.wait_for(
            main.connect_and_serve(main.coinbase_address, producer=kafka_producer, topic=""),
            timeout=10,
        )
    except asyncio.TimeoutError:
        pass

    # make sure we saw some messages
    assert len(kafka_producer.messages) > 0

    # make sure they are valid json
    for message in kafka_producer.messages:
        assert isinstance(json.dumps(json.loads(message)), str)
