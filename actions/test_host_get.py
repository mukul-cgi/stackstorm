import pika
import sys
from st2common.runners.base_action import Action

class TestGetHost(Action):
    def run(self):   
        credentials = pika.PlainCredentials("test", "test")
        parameters = pika.ConnectionParameters('748959631f5b',
                                           5672,
                                           '/',
                                           credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='task_queue1', durable=True)
        
        message = ' '.join(sys.argv[1:]) or "Hello World!"
        
        channel.basic_publish(
            exchange='',
            routing_key='task_queue1',
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()
        print(" [x] Sent %r" % message)
        
