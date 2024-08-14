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

class InteropIdentifierRequestData(object):
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
        'account_id': 'str',
        'id_type': 'str',
        'id_value': 'str',
        'sub_id_or_type': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'id_type': 'idType',
        'id_value': 'idValue',
        'sub_id_or_type': 'subIdOrType'
    }

    def __init__(self, account_id=None, id_type=None, id_value=None, sub_id_or_type=None):  # noqa: E501
        """InteropIdentifierRequestData - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._id_type = None
        self._id_value = None
        self._sub_id_or_type = None
        self.discriminator = None
        self.account_id = account_id
        self.id_type = id_type
        self.id_value = id_value
        if sub_id_or_type is not None:
            self.sub_id_or_type = sub_id_or_type

    @property
    def account_id(self):
        """Gets the account_id of this InteropIdentifierRequestData.  # noqa: E501


        :return: The account_id of this InteropIdentifierRequestData.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InteropIdentifierRequestData.


        :param account_id: The account_id of this InteropIdentifierRequestData.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def id_type(self):
        """Gets the id_type of this InteropIdentifierRequestData.  # noqa: E501


        :return: The id_type of this InteropIdentifierRequestData.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this InteropIdentifierRequestData.


        :param id_type: The id_type of this InteropIdentifierRequestData.  # noqa: E501
        :type: str
        """
        if id_type is None:
            raise ValueError("Invalid value for `id_type`, must not be `None`")  # noqa: E501
        allowed_values = ["MSISDN", "EMAIL", "PERSONAL_ID", "BUSINESS", "DEVICE", "ACCOUNT_ID", "IBAN", "ALIAS", "BBAN"]  # noqa: E501
        if id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(id_type, allowed_values)
            )

        self._id_type = id_type

    @property
    def id_value(self):
        """Gets the id_value of this InteropIdentifierRequestData.  # noqa: E501


        :return: The id_value of this InteropIdentifierRequestData.  # noqa: E501
        :rtype: str
        """
        return self._id_value

    @id_value.setter
    def id_value(self, id_value):
        """Sets the id_value of this InteropIdentifierRequestData.


        :param id_value: The id_value of this InteropIdentifierRequestData.  # noqa: E501
        :type: str
        """
        if id_value is None:
            raise ValueError("Invalid value for `id_value`, must not be `None`")  # noqa: E501

        self._id_value = id_value

    @property
    def sub_id_or_type(self):
        """Gets the sub_id_or_type of this InteropIdentifierRequestData.  # noqa: E501


        :return: The sub_id_or_type of this InteropIdentifierRequestData.  # noqa: E501
        :rtype: str
        """
        return self._sub_id_or_type

    @sub_id_or_type.setter
    def sub_id_or_type(self, sub_id_or_type):
        """Sets the sub_id_or_type of this InteropIdentifierRequestData.


        :param sub_id_or_type: The sub_id_or_type of this InteropIdentifierRequestData.  # noqa: E501
        :type: str
        """

        self._sub_id_or_type = sub_id_or_type

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
        if issubclass(InteropIdentifierRequestData, dict):
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
        if not isinstance(other, InteropIdentifierRequestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
