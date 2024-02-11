#!/bin/bash

# Kafka topic to check
TOPIC_NAME="ticker"

# Kafka namespace (change this if your Kafka is in a different namespace)
KAFKA_NAMESPACE="dev"

# Kafka broker pod name (change this to match your Kafka broker pod name)
KAFKA_POD_NAME=coinbase-cluster-kafka-0

# For stopping when message consumption
TIMEOUT_DURATION=30

# # Command to list all Kafka topics
# echo "Listing all Kafka topics:"
# kubectl exec -n $KAFKA_NAMESPACE $KAFKA_POD_NAME -- /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

# # Command to describe the specific topic
# echo "Describing topic $TOPIC_NAME:"
# kubectl exec -n $KAFKA_NAMESPACE $KAFKA_POD_NAME -- /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic $TOPIC_NAME

# Command to consume messages from the topic (uncomment the line below to use it)
( kubectl exec -i -n $KAFKA_NAMESPACE $KAFKA_POD_NAME -c kafka -- /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic $TOPIC_NAME ) & PID=$!
sleep $TIMEOUT_DURATION
kill $PID