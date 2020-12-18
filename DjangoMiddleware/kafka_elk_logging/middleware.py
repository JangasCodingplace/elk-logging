import binascii
import os
import json
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from datetime import datetime
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable


def log_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


def get_post_data(request):
    data = dict(request.POST)
    if 'password' in data:
        data['password'] = '*********'
    return data


class ResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        try:
            servers = os.getenv('LOG_SERVERS').replace(' ','').split(',')
            self.producer = KafkaProducer(
                bootstrap_servers=servers,
                value_serializer=lambda d: json.dumps(d).encode('utf-8')
            )
        except NoBrokersAvailable:
            self.producer = None


    def __call__(self, request):
        if not self.producer:
            response = self.get_response(request)
            return response

        request_id = generate_key()

        start = now()
        response = self.get_response(request)
        end = now()

        duration = (end - start).total_seconds() * 1000
        try:
            data = response.data
        except AttributeError:
            data = None

        msg = {
            'method': request.META['REQUEST_METHOD'],
            'host': request.META['HTTP_HOST'],
            'path': request.path,
            'params': request.META['QUERY_STRING'],
            'post_data': get_post_data(request),
            'time': datetime.timestamp(now()),
            'duration': "%.3f" % duration,
            'response_body': data,
            'status': response.status_code,
            'request_id': request_id,
        }

        self.producer.send(os.getenv('LOG_TOPIC_NAME'), value=msg)

        response.set_cookie('request_id', request_id)
        return response
