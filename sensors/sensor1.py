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

class HelloSensor(Sensor):
    def setup(self):
        pass

    def run(self):
        while True:
#            payload = {"greeting": "Yo, StackStorm!"}
#            self.sensor_service.dispatch(trigger="test.event2", payload=payload)
            dir = f"/home/test{randint(0,1000)}"
            try:
                os.mkdir(dir)
            except Exception:
                pass
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