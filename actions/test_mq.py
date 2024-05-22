import pika
import time
from st2common.runners.base_action import Action

from kombu import Exchange
#from st2common import config
from st2common.transport.publishers import PoolPublisher

class TestMq(Action):
    def run(self, message):   
        exchange = Exchange('', type="direct")
        publisher = PoolPublisher()
        a = publisher.publish(payload=message, exchange=exchange, routing_key='salt_jobs')
        return a, "message sent"

         
