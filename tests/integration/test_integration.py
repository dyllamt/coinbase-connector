import json

import kafka


def test_integration(kubernetes_services):
    consumer = kafka.KafkaConsumer(
        'ticker',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    )

    for message in consumer:
        print(message)
