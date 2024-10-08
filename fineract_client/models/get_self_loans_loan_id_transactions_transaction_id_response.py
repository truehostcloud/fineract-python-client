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

class GetSelfLoansLoanIdTransactionsTransactionIdResponse(object):
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
        'amount': 'float',
        'currency': 'GetLoanCurrency',
        '_date': 'date',
        'id': 'int',
        'interest_portion': 'float',
        'manually_reversed': 'bool',
        'type': 'GetSelfLoansLoanIdTransactionsType'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        '_date': 'date',
        'id': 'id',
        'interest_portion': 'interestPortion',
        'manually_reversed': 'manuallyReversed',
        'type': 'type'
    }

    def __init__(self, amount=None, currency=None, _date=None, id=None, interest_portion=None, manually_reversed=None, type=None):  # noqa: E501
        """GetSelfLoansLoanIdTransactionsTransactionIdResponse - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._currency = None
        self.__date = None
        self._id = None
        self._interest_portion = None
        self._manually_reversed = None
        self._type = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if _date is not None:
            self._date = _date
        if id is not None:
            self.id = id
        if interest_portion is not None:
            self.interest_portion = interest_portion
        if manually_reversed is not None:
            self.manually_reversed = manually_reversed
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The amount of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.


        :param amount: The amount of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The currency of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: GetLoanCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.


        :param currency: The currency of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: GetLoanCurrency
        """

        self._currency = currency

    @property
    def _date(self):
        """Gets the _date of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The _date of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.


        :param _date: The _date of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def id(self):
        """Gets the id of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The id of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.


        :param id: The id of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_portion(self):
        """Gets the interest_portion of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The interest_portion of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: float
        """
        return self._interest_portion

    @interest_portion.setter
    def interest_portion(self, interest_portion):
        """Sets the interest_portion of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.


        :param interest_portion: The interest_portion of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: float
        """

        self._interest_portion = interest_portion

    @property
    def manually_reversed(self):
        """Gets the manually_reversed of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The manually_reversed of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: bool
        """
        return self._manually_reversed

    @manually_reversed.setter
    def manually_reversed(self, manually_reversed):
        """Sets the manually_reversed of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.


        :param manually_reversed: The manually_reversed of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: bool
        """

        self._manually_reversed = manually_reversed

    @property
    def type(self):
        """Gets the type of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The type of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: GetSelfLoansLoanIdTransactionsType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.


        :param type: The type of this GetSelfLoansLoanIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: GetSelfLoansLoanIdTransactionsType
        """

        self._type = type

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
        if issubclass(GetSelfLoansLoanIdTransactionsTransactionIdResponse, dict):
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
        if not isinstance(other, GetSelfLoansLoanIdTransactionsTransactionIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
