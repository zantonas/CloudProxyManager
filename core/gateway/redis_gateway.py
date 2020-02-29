from core.gateway.abstract_gateway import AbstractGateway
from core import utils

import redis


class RedisGateway(AbstractGateway):
    """
    Gateway to redis memory store.
    Stores data in the following format:
    '<authenticated_user>', '<access_key>,<secret_key>,<endpoint>,<provider_type>'
    """
    def __init__(self):
        """
        Initialize the RedisGateway.
        """
        conf = utils.get_gateway_conf()
        self.r = redis.Redis(host=conf['host'], port=conf['port'])

    def get_storage_credentials(self, user):
        """
        Retrieves the value from redis using the user key.

        :param user: The user
        :return: <access_key>, <secret_key>, <endpoint>, <provider_type>
        """
        try:
            credentials = self.r.get(user).decode('utf-8').split(',', 3)
            return credentials[0], credentials[2], credentials[3]
        except Exception:
            raise Exception('Key not found')

    def set_storage_credentials(self, user, access_key, secret_key,
                                endpoint, provider_type):
        """
        Retrieves the value from redis using the user key.

        :param user: The user.
        :param access_key: The access_key.
        :param secret_key: The secret_key.
        :param endpoint: The endpoint.
        :param provider_type: The provider_type.
        """
        try:
            value = f'{access_key},{secret_key},{endpoint},{provider_type}'
            self.r.set(user, value)
        except Exception as ex:
            raise Exception(ex)

    def delete_storage_credentials(self, user):
        """
        Deletes a record from redis using the user key.
        """
        try:
            self.r.delete(user)
        except Exception as ex:
            raise Exception(ex)
