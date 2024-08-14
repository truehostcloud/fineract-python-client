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

class PaymentType(object):
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
        'id': 'int',
        'is_system_defined': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'is_system_defined': 'isSystemDefined',
        'name': 'name'
    }

    def __init__(self, id=None, is_system_defined=None, name=None):  # noqa: E501
        """PaymentType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._is_system_defined = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if is_system_defined is not None:
            self.is_system_defined = is_system_defined
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this PaymentType.  # noqa: E501


        :return: The id of this PaymentType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentType.


        :param id: The id of this PaymentType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_system_defined(self):
        """Gets the is_system_defined of this PaymentType.  # noqa: E501


        :return: The is_system_defined of this PaymentType.  # noqa: E501
        :rtype: bool
        """
        return self._is_system_defined

    @is_system_defined.setter
    def is_system_defined(self, is_system_defined):
        """Sets the is_system_defined of this PaymentType.


        :param is_system_defined: The is_system_defined of this PaymentType.  # noqa: E501
        :type: bool
        """

        self._is_system_defined = is_system_defined

    @property
    def name(self):
        """Gets the name of this PaymentType.  # noqa: E501


        :return: The name of this PaymentType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentType.


        :param name: The name of this PaymentType.  # noqa: E501
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
        if issubclass(PaymentType, dict):
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
        if not isinstance(other, PaymentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
