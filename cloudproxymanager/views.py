from cloudproxymanager.constants import (HTTP_GET, HTTP_PUT,
                                         HTTP_POST, HTTP_DELETE)
from cloudproxymanager.gateway.redis_gateway import RedisGateway
from flask import request, abort

from flask import Flask
from cloudproxymanager.utils import load_swagger

app = Flask(__name__)
load_swagger(app)


@app.route('/configs/<string:user>/', methods=[HTTP_GET])
def get_config(user):
    """
    Returns the config associated with a user.

    :param user: The user.
    """
    r = RedisGateway()
    try:
        access_key, endpoint, provider_type = r.get_storage_credentials(user)
        response = {'response': {
            'user': user,
            'access_key': access_key,
            'endpoint': endpoint,
            'provider_type': provider_type}
        }
        return response
    except Exception:
        abort(404)


@app.route('/configs/<string:user>/', methods=[HTTP_POST, HTTP_PUT])
def set_config(user):
    """
    Sets the config associated with a user.
    """
    request_json = request.get_json()
    access_key = request_json.get('access_key')
    secret_key = request_json.get('secret_key')
    endpoint = request_json.get('endpoint')
    provider_type = request_json.get('provider_type')
    r = RedisGateway()
    r.set_storage_credentials(user, access_key, secret_key,
                              endpoint, provider_type)
    return {'response': 200}


@app.route('/configs/<string:user>/', methods=[HTTP_DELETE])
def delete_config(user):
    """
    Sets the config associated with a user.
    """
    r = RedisGateway()
    r.delete_storage_credentials(user)
    return {'response': 200}
