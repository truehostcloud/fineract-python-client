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

class GetClientsClientIdTransactionsTransactionIdResponse(object):
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
        'currency': 'GetClientTransactionsCurrency',
        '_date': 'date',
        'id': 'int',
        'office_id': 'int',
        'office_name': 'str',
        'reversed': 'bool',
        'submitted_on_date': 'date',
        'type': 'GetClientsClientIdTransactionsType'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        '_date': 'date',
        'id': 'id',
        'office_id': 'officeId',
        'office_name': 'officeName',
        'reversed': 'reversed',
        'submitted_on_date': 'submittedOnDate',
        'type': 'type'
    }

    def __init__(self, amount=None, currency=None, _date=None, id=None, office_id=None, office_name=None, reversed=None, submitted_on_date=None, type=None):  # noqa: E501
        """GetClientsClientIdTransactionsTransactionIdResponse - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._currency = None
        self.__date = None
        self._id = None
        self._office_id = None
        self._office_name = None
        self._reversed = None
        self._submitted_on_date = None
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
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if reversed is not None:
            self.reversed = reversed
        if submitted_on_date is not None:
            self.submitted_on_date = submitted_on_date
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The amount of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param amount: The amount of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The currency of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: GetClientTransactionsCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param currency: The currency of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: GetClientTransactionsCurrency
        """

        self._currency = currency

    @property
    def _date(self):
        """Gets the _date of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The _date of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param _date: The _date of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def id(self):
        """Gets the id of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The id of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param id: The id of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def office_id(self):
        """Gets the office_id of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The office_id of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param office_id: The office_id of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The office_name of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param office_name: The office_name of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def reversed(self):
        """Gets the reversed of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The reversed of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        """Sets the reversed of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param reversed: The reversed of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: bool
        """

        self._reversed = reversed

    @property
    def submitted_on_date(self):
        """Gets the submitted_on_date of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The submitted_on_date of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: date
        """
        return self._submitted_on_date

    @submitted_on_date.setter
    def submitted_on_date(self, submitted_on_date):
        """Sets the submitted_on_date of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param submitted_on_date: The submitted_on_date of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: date
        """

        self._submitted_on_date = submitted_on_date

    @property
    def type(self):
        """Gets the type of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501


        :return: The type of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :rtype: GetClientsClientIdTransactionsType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetClientsClientIdTransactionsTransactionIdResponse.


        :param type: The type of this GetClientsClientIdTransactionsTransactionIdResponse.  # noqa: E501
        :type: GetClientsClientIdTransactionsType
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
        if issubclass(GetClientsClientIdTransactionsTransactionIdResponse, dict):
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
        if not isinstance(other, GetClientsClientIdTransactionsTransactionIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
