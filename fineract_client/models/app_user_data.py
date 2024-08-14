# coding: utf-8

"""
    Apache Fineract REST API

    Apache Fineract is a secure, multi-tenanted microfinance platform. The goal of the Apache Fineract API is to empower developers to build apps on top of the Apache Fineract Platform. The https://cui.fineract.dev[reference app] (username: mifos, password: password) works on the same demo tenant as the interactive links in this documentation. Until we complete the new REST API documentation you still have the legacy documentation available https://fineract.apache.org/legacy-docs/apiLive.htm[here]. Please check https://fineract.apache.org/docs/current[the Fineract documentation] for more information.  # noqa: E501

    OpenAPI spec version: 1.11.0-SNAPSHOT
    Contact: dev@fineract.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AppUserData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'clients': 'list[ClientData]',
        'row_index': 'int',
        'self_service_user': 'bool'
    }

    attribute_map = {
        'clients': 'clients',
        'row_index': 'rowIndex',
        'self_service_user': 'selfServiceUser'
    }

    def __init__(self, clients=None, row_index=None, self_service_user=None):  # noqa: E501
        """AppUserData - a model defined in Swagger"""  # noqa: E501
        self._clients = None
        self._row_index = None
        self._self_service_user = None
        self.discriminator = None
        if clients is not None:
            self.clients = clients
        if row_index is not None:
            self.row_index = row_index
        if self_service_user is not None:
            self.self_service_user = self_service_user

    @property
    def clients(self):
        """Gets the clients of this AppUserData.  # noqa: E501


        :return: The clients of this AppUserData.  # noqa: E501
        :rtype: list[ClientData]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this AppUserData.


        :param clients: The clients of this AppUserData.  # noqa: E501
        :type: list[ClientData]
        """

        self._clients = clients

    @property
    def row_index(self):
        """Gets the row_index of this AppUserData.  # noqa: E501


        :return: The row_index of this AppUserData.  # noqa: E501
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """Sets the row_index of this AppUserData.


        :param row_index: The row_index of this AppUserData.  # noqa: E501
        :type: int
        """

        self._row_index = row_index

    @property
    def self_service_user(self):
        """Gets the self_service_user of this AppUserData.  # noqa: E501


        :return: The self_service_user of this AppUserData.  # noqa: E501
        :rtype: bool
        """
        return self._self_service_user

    @self_service_user.setter
    def self_service_user(self, self_service_user):
        """Sets the self_service_user of this AppUserData.


        :param self_service_user: The self_service_user of this AppUserData.  # noqa: E501
        :type: bool
        """

        self._self_service_user = self_service_user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AppUserData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppUserData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
