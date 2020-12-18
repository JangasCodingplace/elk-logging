# Elasticsearch

This is a very basic Dockersetup for Elasticsearch. Kibana is not included.
If you want to include Kibana add following lines to `docker-compose` file:

```
kibana:
  image: docker.elastic.co/kibana/kibana:7.9.0
  depends_on:
    - elasticsearch
  ports:
    - "5601:5601"
  environment:
    ELASTICSEARCH_URL: http://elasticsearch:9200
    ELASTICSEARCH_HOSTS: http://elasticsearch:9200
```


## Requirements
The only Requirements are Docker & Docker-Compose.


## Setup
`docker-compose up`

If you'd like to hide the terminal acitivites:

starting Kafka Cluster:
`docker-compose up -d`

stopping Kafka Cluster:
`docker-compose down`


### Important
This is an initial instance for `docker-compose` for elastic search. Here is
no best practice included yet.
