from lib.base import ZabbixBaseAction

class TestGetHost(ZabbixBaseAction):
    def run(self, customer_id, host_id):   
        self.fetch_config(customer_id)
        #zabbix_url = customer_config['zabbix_url']
        #api_key = customer_config['api_key']

        params = {"hostids": host_id}
        #data = {"jsonrpc": "2.0", "method": "host.get", "params": params, "id": 1, "auth": api_key}
    
        #return self.make_request(method="get", url=zabbix_url, data=data)
    
        return self.make_request(
            http_method="get", 
            api_method="host.get", 
            params=params, 
            )


