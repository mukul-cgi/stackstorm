import pika
import time
from st2common.runners.base_action import Action

from kombu import Connection, Exchange, Consumer, Queue
#from st2common import config
from st2common.transport.publishers import PoolPublisher

class TestMq(Action):
    def process_message(self, body, message):
#        print("body is {body}")
#        payload = {"message_body": "{body}"}
#        self.sensor_service.dispatch(trigger="test.event2", payload=payload, trace_tag="tag123")
        message.ack()
        print(body)
        return body
    
    def run(self, message):   
        exchange = Exchange('', type="direct")
        publisher = PoolPublisher()
        a = publisher.publish(payload=message, exchange=exchange, routing_key='salt_jobs')
        
        rabbit_url = "amqp://guest:guest@rabbitmq:5672"
        conn = Connection(rabbit_url)
        exchange = Exchange("", type="direct")
        queue = Queue(name="salt_finished", exchange=exchange, routing_key="salt_finished")
        consumer = Consumer(conn, queues=queue, callbacks=[self.process_message], accept=['application/json', 'application/x-python-serialize', 'pickle'])
        consumer.consume()
