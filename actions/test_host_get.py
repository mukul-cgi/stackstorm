import requests
import json
from st2common.runners.base_action import Action

class TestGetHost(Action):
    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def run(self, customer_id, host_id):   
        zabbix_url = self.config['test_zabbix'][customer_id]['zabbix_url']
        api_key = self.config['test_zabbix'][customer_id]['api_key']

        params = {"hostids": host_id}
        data = {"jsonrpc": "2.0", "method": "host.get", "params": params, "id": 1, "auth": api_key}
        data = json.dumps(data)

        output = requests.get(url=zabbix_url, data=data, headers={'Content-Type': 'application/json-rpc'} )
        
        return output.json()