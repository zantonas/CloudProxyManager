import requests


def get_user_details(user='user'):
    """
    Returns the config associated with the user.

    :param user: The user key
    """
    r = requests.get(f'http://127.0.0.2:5000/configs/{user}')
    print(r)
    print(r.text)


def set_user_details(user='user', access_key='my_access_key', secret_key='secret_key',
                     endpoint='endpoint', provider_type='provider_type'):
    """
    Sets the config associated with the user.

    :param user: The user.
    :param access_key: The access_key.
    :param secret_key: The secret_key.
    :param endpoint: The endpoint.
    :param provider_type: The provider_type.
    """
    r = requests.post(f'http://127.0.0.2:5000/configs/{user}',
                      json={'user': user,
                            'access_key': access_key,
                            'secret_key': secret_key,
                            'endpoint': endpoint,
                            'provider_type': provider_type}
                      )
    print(r)
    print(r.text)


def delete_user_details(user='user'):
    """
    Deletes the config associated with the user.

    :param user: The user key
    """
    r = requests.delete(f'http://127.0.0.2:5000/configs/{user}')
    print(r)
    print(r.text)
