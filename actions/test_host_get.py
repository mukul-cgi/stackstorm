from lib.base import ZabbixBaseAction

class TestGetHost(ZabbixBaseAction):
    def run(self, customer_id, host_id, test):   
        self.fetch_config(customer_id)

        params = {"12": host_id, "11": "123"}

        return self.make_request(
            http_method="post", 
            api_method="host.get", 
            params=params, 
            )
