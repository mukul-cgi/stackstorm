import requests
import json
from st2common.runners.base_action import Action

class ZabbixBaseAction(Action):
    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def fetch_config(self, customer_id):
        customer_config = self.config['test_zabbix'].get(customer_id)
        if customer_config:
            if 'zabbix_url' not in customer_config:
                raise ValueError("Zabbix url details not found in config.yaml")
            elif 'api_key' not in customer_config:
                raise ValueError("Zabbix token details not found in config.yaml")
        else:
            raise ValueError(f"Config data for input customer id - {customer_id} not found in config.yaml")
        
        return Zabbix(customer_config['zabbix_url'], customer_config['api_key'])

class Zabbix:
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def __enter__(self):
        self.session = requests.session()
        #return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.session.close()

    def make_request(self, http_method, api_method, params):
        #data = json.dumps(data)
        headers={'Content-Type': 'application/json-rpc'}
        data = {"jsonrpc": "2.0", "method": api_method, "params": params, "id": 1, "auth": self.key}
        response = requests.request(
            method=http_method,
            url=self.url,
            json=data,
            headers=headers,
        )
        
        ret = response.json()
        if "error" in ret:
            raise Exception(ret["error"])
        
        return ret["result"]