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

class PutRecurringDepositAccountsChanges(object):
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
        'deposit_amount': 'int',
        'locale': 'str'
    }

    attribute_map = {
        'deposit_amount': 'depositAmount',
        'locale': 'locale'
    }

    def __init__(self, deposit_amount=None, locale=None):  # noqa: E501
        """PutRecurringDepositAccountsChanges - a model defined in Swagger"""  # noqa: E501
        self._deposit_amount = None
        self._locale = None
        self.discriminator = None
        if deposit_amount is not None:
            self.deposit_amount = deposit_amount
        if locale is not None:
            self.locale = locale

    @property
    def deposit_amount(self):
        """Gets the deposit_amount of this PutRecurringDepositAccountsChanges.  # noqa: E501


        :return: The deposit_amount of this PutRecurringDepositAccountsChanges.  # noqa: E501
        :rtype: int
        """
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, deposit_amount):
        """Sets the deposit_amount of this PutRecurringDepositAccountsChanges.


        :param deposit_amount: The deposit_amount of this PutRecurringDepositAccountsChanges.  # noqa: E501
        :type: int
        """

        self._deposit_amount = deposit_amount

    @property
    def locale(self):
        """Gets the locale of this PutRecurringDepositAccountsChanges.  # noqa: E501


        :return: The locale of this PutRecurringDepositAccountsChanges.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PutRecurringDepositAccountsChanges.


        :param locale: The locale of this PutRecurringDepositAccountsChanges.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if issubclass(PutRecurringDepositAccountsChanges, dict):
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
        if not isinstance(other, PutRecurringDepositAccountsChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
