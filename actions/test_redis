import redis
from st2common.runners.base_action import Action

class TestRedis(Action):
    def run(self):   
        redis_client = redis.Redis(host='a0382acdcbda', port=6379, db=0)         
        redis_client.set('key', 'value')
        data = redis_client.get('key')
        return data
        
