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

class ChargeToGLAccountMapper(object):
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
        'charge': 'ChargeData',
        'income_account': 'GLAccountData'
    }

    attribute_map = {
        'charge': 'charge',
        'income_account': 'incomeAccount'
    }

    def __init__(self, charge=None, income_account=None):  # noqa: E501
        """ChargeToGLAccountMapper - a model defined in Swagger"""  # noqa: E501
        self._charge = None
        self._income_account = None
        self.discriminator = None
        if charge is not None:
            self.charge = charge
        if income_account is not None:
            self.income_account = income_account

    @property
    def charge(self):
        """Gets the charge of this ChargeToGLAccountMapper.  # noqa: E501


        :return: The charge of this ChargeToGLAccountMapper.  # noqa: E501
        :rtype: ChargeData
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this ChargeToGLAccountMapper.


        :param charge: The charge of this ChargeToGLAccountMapper.  # noqa: E501
        :type: ChargeData
        """

        self._charge = charge

    @property
    def income_account(self):
        """Gets the income_account of this ChargeToGLAccountMapper.  # noqa: E501


        :return: The income_account of this ChargeToGLAccountMapper.  # noqa: E501
        :rtype: GLAccountData
        """
        return self._income_account

    @income_account.setter
    def income_account(self, income_account):
        """Sets the income_account of this ChargeToGLAccountMapper.


        :param income_account: The income_account of this ChargeToGLAccountMapper.  # noqa: E501
        :type: GLAccountData
        """

        self._income_account = income_account

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
        if issubclass(ChargeToGLAccountMapper, dict):
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
        if not isinstance(other, ChargeToGLAccountMapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
