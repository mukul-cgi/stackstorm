import redis
import os
import requests
from st2common.runners.base_action import Action
from st2common.transport import utils as transport_utils
#from common import test
import raas_common
#from raas_common import RaasBaseAction, publish_message, queue_consumer

class TestRedis(Action):
    def run(self):   
 #       redis_client = redis.Redis(host='a0382acdcbda', port=6379, db=0)         
 #       redis_client.set('key', 'value')
 #       data = redis_client.get('key')
 #       key = os.environ['ST2_ACTION_AUTH_TOKEN']
 #       base_url = os.environ['ST2_ACTION_API_URL']
 #       api_url = f"{base_url}/traces/?trace_tag=tag123"
 #       headers = {
 #           'Accept': 'application/json',
 #           'X-Auth-Token': key
 #       }
 #       ret = requests.get(url=api_url, headers=headers)
        return raas_common.config_check()
        
