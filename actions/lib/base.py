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
            raise ValueError("Config data for input customer id - customer_id not found in config.yaml")
        
        return { "zabbix_url": customer_config['zabbix_url'],
                 "api_key": customer_config['api_key']
        }
