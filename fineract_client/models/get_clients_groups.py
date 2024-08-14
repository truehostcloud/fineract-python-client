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

class GetClientsGroups(object):
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
        'account_no': 'str',
        'external_id': 'int',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'external_id': 'externalId',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, account_no=None, external_id=None, id=None, name=None):  # noqa: E501
        """GetClientsGroups - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._external_id = None
        self._id = None
        self._name = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def account_no(self):
        """Gets the account_no of this GetClientsGroups.  # noqa: E501


        :return: The account_no of this GetClientsGroups.  # noqa: E501
        :rtype: str
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GetClientsGroups.


        :param account_no: The account_no of this GetClientsGroups.  # noqa: E501
        :type: str
        """

        self._account_no = account_no

    @property
    def external_id(self):
        """Gets the external_id of this GetClientsGroups.  # noqa: E501


        :return: The external_id of this GetClientsGroups.  # noqa: E501
        :rtype: int
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this GetClientsGroups.


        :param external_id: The external_id of this GetClientsGroups.  # noqa: E501
        :type: int
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this GetClientsGroups.  # noqa: E501


        :return: The id of this GetClientsGroups.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetClientsGroups.


        :param id: The id of this GetClientsGroups.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetClientsGroups.  # noqa: E501


        :return: The name of this GetClientsGroups.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetClientsGroups.


        :param name: The name of this GetClientsGroups.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(GetClientsGroups, dict):
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
        if not isinstance(other, GetClientsGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
