import requests
import json
#from st2common.runners.base_action import Action

class TestGetHost():
    def __init__(self, config):
#        super().__init__(config)
        self.config = config

    def run(self, customer_id, host_id):
        
        for each in self.config['test_zabbix']:
            if customer_id == each['customer_id']:
                zabbix_url = each['zabbix_url']
                api_key = each['api_key']

        params = {"hostids": host_id}
        data = {"jsonrpc": "2.0", "method": "host.get", "params": params, "id": 1, "auth": api_key}

        data = json.dumps(data)

        output = requests.get(url=zabbix_url, data=data, headers={'Content-Type': 'application/json-rpc'} )
        return output.json()