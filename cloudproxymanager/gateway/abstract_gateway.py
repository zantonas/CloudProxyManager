from abc import ABC, abstractmethod


class AbstractGateway(ABC):
    """
    Gateway to an abstract data store.
    """

    @abstractmethod
    def get_storage_credentials(self, user):
        """
        Retrieves the value from the gateway using the user key.

        :param user: The user.
        """
        pass

    @abstractmethod
    def set_storage_credentials(self, user, access_key, secret_key,
                                endpoint, provider_type):
        """
        Sets the value from the gateway using the user key.

        :param user: The user.
        :param access_key: The access_key.
        :param secret_key: The secret_key.
        :param endpoint: The endpoint.
        :param provider_type: The provider_type.
        """
        pass

    @abstractmethod
    def delete_storage_credentials(self, user):
        """
        Deletes the record from the gateway using the user key.

        :param user: The user.
        """
        pass
