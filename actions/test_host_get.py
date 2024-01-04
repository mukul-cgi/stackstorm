import requests
import json
from lib.base import ZabbixBaseAction

class TestGetHost(ZabbixBaseAction):
    def run(self, customer_id, host_id):   
        customer_config = super().fetch_config(customer_id)
        zabbix_url = customer_config['zabbix_url']
        api_key = customer_config['api_key']

        params = {"hostids": host_id}
        data = {"jsonrpc": "2.0", "method": "host.get", "params": params, "id": 1, "auth": api_key}
        data = json.dumps(data)
        
        return self.make_request(method="get", url=zabbix_url, data=data)
    
    def make_request(self, method, url, data):
        headers={'Content-Type': 'application/json-rpc'}
        response = requests.request(
            method=method,
            url=url,
            data=data,
            headers=headers,
        )

        return response.json()

