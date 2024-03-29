from lib.base import ZabbixBaseAction

class TestGetHost(ZabbixBaseAction):
    def run(self, customer_id, host_id, test):   
        obj =  self.fetch_config(customer_id)

        params = {"hostids": host_id}

        return obj.make_request(
            http_method="post", 
            api_method="host.get", 
            params=params, 
            )