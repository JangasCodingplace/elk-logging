# Apache Kafka Logging Setup

This is a very basic Apache Single-Node Kafka Setup for Logging activities.
It's based on Wurstmeister Image - take a look to the official repository:

https://github.com/wurstmeister/kafka-docker


## Requirements
The only Requirements are Docker & Docker-Compose.


## Setup
`docker-compose up`

If you'd like to hide the terminal acitivites:

starting Kafka Cluster:
`docker-compose up -d`

stopping Kafka Cluster:
`docker-compose down`


## About Kafka
Apache Kafka is a high scalable open source stream-processing tool. It's used
for processing big data streams or as message system to connect microservices.

You can scale that cluster by adding multiple nodes.
You can secure that cluster by adding replications.

__Please note__ This is an initial try for including a kafka architecture.
It's not tested yet and no best practices are included yet.
