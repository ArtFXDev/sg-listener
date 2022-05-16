import json

from decouple import config
from pika import BlockingConnection
from pika import ConnectionParameters

BROKER_URL = config("BROKER_URL")
BROKER_EXCHANGE_NAME = config("BROKER_EXCHANGE_NAME")
SG_WORKER_QUEUE_NAME = config("SG_WORKER_QUEUE_NAME")


def digest_event(channel, delivery, properties, payload):
    dispatch_event(delivery.routing_key, json.loads(payload))
    channel.basic_ack(delivery_tag=delivery.delivery_tag)


def dispatch_event(routing_key, payload):
    print("synch shotgun with", routing_key, payload)


params = ConnectionParameters(BROKER_URL)
connection = BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange=BROKER_EXCHANGE_NAME, exchange_type='topic')
channel.queue_declare(queue=WORKER_QUEUE_NAME, durable=True)
channel.queue_bind(exchange=BROKER_EXCHANGE_NAME, queue=WORKER_QUEUE_NAME, routing_key="#")
channel.basic_qos(prefetch_count=20)
channel.basic_consume(queue=WORKER_QUEUE_NAME, on_message_callback=digest_event)

channel.start_consuming()
