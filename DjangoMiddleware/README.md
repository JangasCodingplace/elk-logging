# Django Response Logging Middleware
This is a Middleware for logging any human-made responses at any Django
application. Usecases for this Middleware can be
- Logging
- Debugging

This Middleware works fine with Apache Kafka + ELK Stack.

It's a full reusable component.
Its collecting request and response informations about:
- Request Type
- host
- path
- get parameters
- post parameters
- response status
- response body
- request-ip address
- request time
- execution time between request & response
- request_id

The middleware place a request_id in responses cookies for having a better
debugging experience to communicate to distributed developing teams. It's just
used for finding fast matches if some requests fails.


## Requirements
- a running Kafka Cluster


## Setup
Copy the `kafka_elk_logging` directory into a django project. Update your
`.env` settings by including
- LOG_SERVERS = localhost:9092
- LOG_TOPIC_NAME = response-logging

Following packages needs to be installed within your Django project:
- kafka-python
- python-loadenv

_take a look into `requirements.txt`_

After following these instructions you need to update your settings file:
```
MIDDLEWARE = [
    ...
    'kafka_elk_logging.middleware.ResponseLoggingMiddleware',
    ...
]
```

### Please Note
This is an raw, untested & initial version for logging activities.
_It's not tested for `async views`._
