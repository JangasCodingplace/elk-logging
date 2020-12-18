# Logstash

Here is nothing included yet. Go to https://www.elastic.co/de/downloads/logstash
download zip-file for your system and follow instructions.

Replace default `logstash.conf` file with `logstash.conf` file of this
directory. As an alternative you can also copy the basic lines:

```
input {
  kafka {
    bootstrap_servers => "localhost:9092"
    topics => "response-logging"
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "response-logging"
    workers => 1
  }
}
```

## Setup
Kafka Cluster and Elasticsearch needs to be started & running before you are
starting Logstash.

Please spend attention on topic name in `logstash.conf` file and make sure that
you have configured it correctly.
