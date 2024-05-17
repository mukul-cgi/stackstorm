import pika
import time
from st2common.runners.base_action import Action

class TestMq(Action):
    def run(self):   
#        credentials = pika.PlainCredentials("test", "test")
        parameters = pika.ConnectionParameters('748959631f5b',
                                           5672,
                                           '/',
                                           )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='task_queue1', durable=True)
        
        message = "Hello World!"
        
        channel.basic_publish(
            exchange='',
            routing_key='task_queue1',
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()
        time.sleep(20)
        return f"[x] Sent {message}"
        
