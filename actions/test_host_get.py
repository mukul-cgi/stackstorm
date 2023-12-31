import requests
import json
from st2common.runners.base_action import Action

class TestGetHost(Action):

    zabbix_url = "http://a03a00d009d6:8080/api_jsonrpc.php"
    api_key = "b62ffb555daf420447e17c7105b8307e85ee1962ab920692b8c5ec0e97b79dd7"

    def __init__(self, config):
        super(ZabbixBaseAction, self).__init__(config)

        self.config = config

    def run(self, host_id=None):
        params = {"hostids": host_id}
        data = {"jsonrpc": "2.0", "method": "host.get", "params": params, "id": 1, "auth": self.api_key}

        data = json.dumps(data)

        output = requests.get(url=self.zabbix_url, data=data, headers={'Content-Type': 'application/json-rpc'} )

        return output.json()