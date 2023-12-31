import requests
import json
from st2common.runners.base_action import Action

class TestGetHost(Action):
    def __init__(self, config):
        super(TestGetHost, self).__init__(config)
        self.config = config

    def run(self, zabbix_url, api_key, host_id):
        params = {"hostids": host_id}
        data = {"jsonrpc": "2.0", "method": "host.get", "params": params, "id": 1, "auth": api_key}

        data = json.dumps(data)

        output = requests.get(url=zabbix_url, data=data, headers={'Content-Type': 'application/json-rpc'} )

        return output.json()