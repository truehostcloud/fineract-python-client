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

class PostFixedDepositAccountsRequest(object):
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
        'client_id': 'int',
        'date_format': 'str',
        'deposit_amount': 'float',
        'deposit_period': 'int',
        'deposit_period_frequency_id': 'int',
        'locale': 'str',
        'product_id': 'int',
        'submitted_on_date': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'date_format': 'dateFormat',
        'deposit_amount': 'depositAmount',
        'deposit_period': 'depositPeriod',
        'deposit_period_frequency_id': 'depositPeriodFrequencyId',
        'locale': 'locale',
        'product_id': 'productId',
        'submitted_on_date': 'submittedOnDate'
    }

    def __init__(self, client_id=None, date_format=None, deposit_amount=None, deposit_period=None, deposit_period_frequency_id=None, locale=None, product_id=None, submitted_on_date=None):  # noqa: E501
        """PostFixedDepositAccountsRequest - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._date_format = None
        self._deposit_amount = None
        self._deposit_period = None
        self._deposit_period_frequency_id = None
        self._locale = None
        self._product_id = None
        self._submitted_on_date = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if date_format is not None:
            self.date_format = date_format
        if deposit_amount is not None:
            self.deposit_amount = deposit_amount
        if deposit_period is not None:
            self.deposit_period = deposit_period
        if deposit_period_frequency_id is not None:
            self.deposit_period_frequency_id = deposit_period_frequency_id
        if locale is not None:
            self.locale = locale
        if product_id is not None:
            self.product_id = product_id
        if submitted_on_date is not None:
            self.submitted_on_date = submitted_on_date

    @property
    def client_id(self):
        """Gets the client_id of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The client_id of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this PostFixedDepositAccountsRequest.


        :param client_id: The client_id of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def date_format(self):
        """Gets the date_format of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The date_format of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostFixedDepositAccountsRequest.


        :param date_format: The date_format of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def deposit_amount(self):
        """Gets the deposit_amount of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The deposit_amount of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: float
        """
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, deposit_amount):
        """Sets the deposit_amount of this PostFixedDepositAccountsRequest.


        :param deposit_amount: The deposit_amount of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: float
        """

        self._deposit_amount = deposit_amount

    @property
    def deposit_period(self):
        """Gets the deposit_period of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The deposit_period of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._deposit_period

    @deposit_period.setter
    def deposit_period(self, deposit_period):
        """Sets the deposit_period of this PostFixedDepositAccountsRequest.


        :param deposit_period: The deposit_period of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: int
        """

        self._deposit_period = deposit_period

    @property
    def deposit_period_frequency_id(self):
        """Gets the deposit_period_frequency_id of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The deposit_period_frequency_id of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._deposit_period_frequency_id

    @deposit_period_frequency_id.setter
    def deposit_period_frequency_id(self, deposit_period_frequency_id):
        """Sets the deposit_period_frequency_id of this PostFixedDepositAccountsRequest.


        :param deposit_period_frequency_id: The deposit_period_frequency_id of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: int
        """

        self._deposit_period_frequency_id = deposit_period_frequency_id

    @property
    def locale(self):
        """Gets the locale of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The locale of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostFixedDepositAccountsRequest.


        :param locale: The locale of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def product_id(self):
        """Gets the product_id of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The product_id of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PostFixedDepositAccountsRequest.


        :param product_id: The product_id of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def submitted_on_date(self):
        """Gets the submitted_on_date of this PostFixedDepositAccountsRequest.  # noqa: E501


        :return: The submitted_on_date of this PostFixedDepositAccountsRequest.  # noqa: E501
        :rtype: str
        """
        return self._submitted_on_date

    @submitted_on_date.setter
    def submitted_on_date(self, submitted_on_date):
        """Sets the submitted_on_date of this PostFixedDepositAccountsRequest.


        :param submitted_on_date: The submitted_on_date of this PostFixedDepositAccountsRequest.  # noqa: E501
        :type: str
        """

        self._submitted_on_date = submitted_on_date

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
        if issubclass(PostFixedDepositAccountsRequest, dict):
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
        if not isinstance(other, PostFixedDepositAccountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
