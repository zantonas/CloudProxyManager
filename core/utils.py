import json


def get_gateway_conf():
    """
    Returns the gateway config.
    """
    with open('conf/gateway.json') as f:
        return json.load(f)
