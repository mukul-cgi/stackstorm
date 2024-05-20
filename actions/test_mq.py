import pika
import time
from st2common.runners.base_action import Action

import eventlet
from kombu import Exchange

from st2common import config
from st2common.transport.publishers import PoolPublisher

class TestMq(Action):
    def run(self):   
#        credentials = pika.PlainCredentials("test", "test")
#        parameters = pika.ConnectionParameters('748959631f5b',
#                                           5672,
#                                           '/',
#                                           )
#        connection = pika.BlockingConnection(parameters)
#        channel = connection.channel()
#        channel.queue_declare(queue='task_queue1', durable=True)
        
#        message = "Hello World!"
        
#        channel.basic_publish(
#            exchange='',
#            routing_key='task_queue1',
#            body=message,
#            properties=pika.BasicProperties(delivery_mode=2)
#        )
#        connection.close()
#        time.sleep(20)
#        return f"[x] Sent {message}"
        exchange = Exchange('amq.direct', type="direct")
        
        publisher = PoolPublisher()
        publisher.publish(payload='test_message', exchange=exchange, routing_key='task_queue1')
        eventlet.sleep(0.5)
        return "message sent"

         
