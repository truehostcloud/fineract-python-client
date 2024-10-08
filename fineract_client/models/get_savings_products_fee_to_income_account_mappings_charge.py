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

class GetSavingsProductsFeeToIncomeAccountMappingsCharge(object):
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
        'active': 'bool',
        'id': 'int',
        'name': 'str',
        'penalty': 'bool'
    }

    attribute_map = {
        'active': 'active',
        'id': 'id',
        'name': 'name',
        'penalty': 'penalty'
    }

    def __init__(self, active=None, id=None, name=None, penalty=None):  # noqa: E501
        """GetSavingsProductsFeeToIncomeAccountMappingsCharge - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._id = None
        self._name = None
        self._penalty = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if penalty is not None:
            self.penalty = penalty

    @property
    def active(self):
        """Gets the active of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501


        :return: The active of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.


        :param active: The active of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def id(self):
        """Gets the id of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501


        :return: The id of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.


        :param id: The id of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501


        :return: The name of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.


        :param name: The name of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def penalty(self):
        """Gets the penalty of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501


        :return: The penalty of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :rtype: bool
        """
        return self._penalty

    @penalty.setter
    def penalty(self, penalty):
        """Sets the penalty of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.


        :param penalty: The penalty of this GetSavingsProductsFeeToIncomeAccountMappingsCharge.  # noqa: E501
        :type: bool
        """

        self._penalty = penalty

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
        if issubclass(GetSavingsProductsFeeToIncomeAccountMappingsCharge, dict):
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
        if not isinstance(other, GetSavingsProductsFeeToIncomeAccountMappingsCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
