# Copyright 2020 The StackStorm Authors.
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import eventlet

from st2reactor.sensor.base import Sensor
import os 
from random import randint
from kombu import Connection, Exchange, Queue, Consumer


        
class HelloSensor(Sensor):  
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
    def setup(self):
        rabbit_url = "amqp://guest:guest@rabbitmq:5672"
        self.conn = Connection(rabbit_url)
        exchange = Exchange("", type="direct")
        self.queue = Queue(name="salt_jobs", exchange=exchange, routing_key="salt_jobs")
        self.consumer = Consumer(self.conn, queues=self.queue, callbacks=[self.process_message], accept=['application/json', 'application/x-python-serialize', 'pickle'])
        self.consumer.consume()

    def process_message(self, body, message):
        print("body is {body}")
#        payload = {"message_body": "{body}"}
#        self.sensor_service.dispatch(trigger="test.event2", payload=payload)
        self.logger.debug(f"message body - {body}")
        message.ack()

    def run(self):
        while True:

            self.conn.drain_events()
            eventlet.sleep(10)

    def cleanup(self):
        pass

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
