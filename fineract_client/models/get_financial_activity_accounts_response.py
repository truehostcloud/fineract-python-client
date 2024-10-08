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

class GetFinancialActivityAccountsResponse(object):
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
        'financial_activity_data': 'FinancialActivityData',
        'gl_account_data': 'GLAccountData',
        'id': 'int'
    }

    attribute_map = {
        'financial_activity_data': 'financialActivityData',
        'gl_account_data': 'glAccountData',
        'id': 'id'
    }

    def __init__(self, financial_activity_data=None, gl_account_data=None, id=None):  # noqa: E501
        """GetFinancialActivityAccountsResponse - a model defined in Swagger"""  # noqa: E501
        self._financial_activity_data = None
        self._gl_account_data = None
        self._id = None
        self.discriminator = None
        if financial_activity_data is not None:
            self.financial_activity_data = financial_activity_data
        if gl_account_data is not None:
            self.gl_account_data = gl_account_data
        if id is not None:
            self.id = id

    @property
    def financial_activity_data(self):
        """Gets the financial_activity_data of this GetFinancialActivityAccountsResponse.  # noqa: E501


        :return: The financial_activity_data of this GetFinancialActivityAccountsResponse.  # noqa: E501
        :rtype: FinancialActivityData
        """
        return self._financial_activity_data

    @financial_activity_data.setter
    def financial_activity_data(self, financial_activity_data):
        """Sets the financial_activity_data of this GetFinancialActivityAccountsResponse.


        :param financial_activity_data: The financial_activity_data of this GetFinancialActivityAccountsResponse.  # noqa: E501
        :type: FinancialActivityData
        """

        self._financial_activity_data = financial_activity_data

    @property
    def gl_account_data(self):
        """Gets the gl_account_data of this GetFinancialActivityAccountsResponse.  # noqa: E501


        :return: The gl_account_data of this GetFinancialActivityAccountsResponse.  # noqa: E501
        :rtype: GLAccountData
        """
        return self._gl_account_data

    @gl_account_data.setter
    def gl_account_data(self, gl_account_data):
        """Sets the gl_account_data of this GetFinancialActivityAccountsResponse.


        :param gl_account_data: The gl_account_data of this GetFinancialActivityAccountsResponse.  # noqa: E501
        :type: GLAccountData
        """

        self._gl_account_data = gl_account_data

    @property
    def id(self):
        """Gets the id of this GetFinancialActivityAccountsResponse.  # noqa: E501


        :return: The id of this GetFinancialActivityAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetFinancialActivityAccountsResponse.


        :param id: The id of this GetFinancialActivityAccountsResponse.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(GetFinancialActivityAccountsResponse, dict):
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
        if not isinstance(other, GetFinancialActivityAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
