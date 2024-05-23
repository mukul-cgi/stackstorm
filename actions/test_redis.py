import redis
import os
from st2common.runners.base_action import Action
from st2common.transport import utils as transport_utils

class TestRedis(Action):
    def run(self):   
 #       redis_client = redis.Redis(host='a0382acdcbda', port=6379, db=0)         
 #       redis_client.set('key', 'value')
 #       data = redis_client.get('key')
        key = os.environ['ST2_ACTION_AUTH_TOKEN']
        return key
        
