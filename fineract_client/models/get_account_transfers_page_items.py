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

class GetAccountTransfersPageItems(object):
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
        'currency': 'GetAccountTransfersPageItemsCurrency',
        'from_account': 'GetAccountTransfersPageItemsFromAccount',
        'from_account_type': 'GetAccountTransfersFromAccountType',
        'from_client': 'GetAccountTransfersFromClientOptions',
        'from_office': 'GetAccountTransfersPageItemsFromOffice',
        'id': 'int',
        'reversed': 'bool',
        'to_account': 'GetAccountTransfersPageItemsFromAccount',
        'to_account_type': 'GetAccountTransfersPageItemsToAccountType',
        'to_client': 'GetAccountTransfersFromClientOptions',
        'to_office': 'GetAccountTransfersPageItemsFromOffice',
        'transfer_amount': 'float',
        'transfer_date': 'date',
        'transfer_description': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'from_account': 'fromAccount',
        'from_account_type': 'fromAccountType',
        'from_client': 'fromClient',
        'from_office': 'fromOffice',
        'id': 'id',
        'reversed': 'reversed',
        'to_account': 'toAccount',
        'to_account_type': 'toAccountType',
        'to_client': 'toClient',
        'to_office': 'toOffice',
        'transfer_amount': 'transferAmount',
        'transfer_date': 'transferDate',
        'transfer_description': 'transferDescription'
    }

    def __init__(self, currency=None, from_account=None, from_account_type=None, from_client=None, from_office=None, id=None, reversed=None, to_account=None, to_account_type=None, to_client=None, to_office=None, transfer_amount=None, transfer_date=None, transfer_description=None):  # noqa: E501
        """GetAccountTransfersPageItems - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._from_account = None
        self._from_account_type = None
        self._from_client = None
        self._from_office = None
        self._id = None
        self._reversed = None
        self._to_account = None
        self._to_account_type = None
        self._to_client = None
        self._to_office = None
        self._transfer_amount = None
        self._transfer_date = None
        self._transfer_description = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if from_account is not None:
            self.from_account = from_account
        if from_account_type is not None:
            self.from_account_type = from_account_type
        if from_client is not None:
            self.from_client = from_client
        if from_office is not None:
            self.from_office = from_office
        if id is not None:
            self.id = id
        if reversed is not None:
            self.reversed = reversed
        if to_account is not None:
            self.to_account = to_account
        if to_account_type is not None:
            self.to_account_type = to_account_type
        if to_client is not None:
            self.to_client = to_client
        if to_office is not None:
            self.to_office = to_office
        if transfer_amount is not None:
            self.transfer_amount = transfer_amount
        if transfer_date is not None:
            self.transfer_date = transfer_date
        if transfer_description is not None:
            self.transfer_description = transfer_description

    @property
    def currency(self):
        """Gets the currency of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The currency of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersPageItemsCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetAccountTransfersPageItems.


        :param currency: The currency of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersPageItemsCurrency
        """

        self._currency = currency

    @property
    def from_account(self):
        """Gets the from_account of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The from_account of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersPageItemsFromAccount
        """
        return self._from_account

    @from_account.setter
    def from_account(self, from_account):
        """Sets the from_account of this GetAccountTransfersPageItems.


        :param from_account: The from_account of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersPageItemsFromAccount
        """

        self._from_account = from_account

    @property
    def from_account_type(self):
        """Gets the from_account_type of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The from_account_type of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersFromAccountType
        """
        return self._from_account_type

    @from_account_type.setter
    def from_account_type(self, from_account_type):
        """Sets the from_account_type of this GetAccountTransfersPageItems.


        :param from_account_type: The from_account_type of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersFromAccountType
        """

        self._from_account_type = from_account_type

    @property
    def from_client(self):
        """Gets the from_client of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The from_client of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersFromClientOptions
        """
        return self._from_client

    @from_client.setter
    def from_client(self, from_client):
        """Sets the from_client of this GetAccountTransfersPageItems.


        :param from_client: The from_client of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersFromClientOptions
        """

        self._from_client = from_client

    @property
    def from_office(self):
        """Gets the from_office of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The from_office of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersPageItemsFromOffice
        """
        return self._from_office

    @from_office.setter
    def from_office(self, from_office):
        """Sets the from_office of this GetAccountTransfersPageItems.


        :param from_office: The from_office of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersPageItemsFromOffice
        """

        self._from_office = from_office

    @property
    def id(self):
        """Gets the id of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The id of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAccountTransfersPageItems.


        :param id: The id of this GetAccountTransfersPageItems.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reversed(self):
        """Gets the reversed of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The reversed of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        """Sets the reversed of this GetAccountTransfersPageItems.


        :param reversed: The reversed of this GetAccountTransfersPageItems.  # noqa: E501
        :type: bool
        """

        self._reversed = reversed

    @property
    def to_account(self):
        """Gets the to_account of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The to_account of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersPageItemsFromAccount
        """
        return self._to_account

    @to_account.setter
    def to_account(self, to_account):
        """Sets the to_account of this GetAccountTransfersPageItems.


        :param to_account: The to_account of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersPageItemsFromAccount
        """

        self._to_account = to_account

    @property
    def to_account_type(self):
        """Gets the to_account_type of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The to_account_type of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersPageItemsToAccountType
        """
        return self._to_account_type

    @to_account_type.setter
    def to_account_type(self, to_account_type):
        """Sets the to_account_type of this GetAccountTransfersPageItems.


        :param to_account_type: The to_account_type of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersPageItemsToAccountType
        """

        self._to_account_type = to_account_type

    @property
    def to_client(self):
        """Gets the to_client of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The to_client of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersFromClientOptions
        """
        return self._to_client

    @to_client.setter
    def to_client(self, to_client):
        """Sets the to_client of this GetAccountTransfersPageItems.


        :param to_client: The to_client of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersFromClientOptions
        """

        self._to_client = to_client

    @property
    def to_office(self):
        """Gets the to_office of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The to_office of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: GetAccountTransfersPageItemsFromOffice
        """
        return self._to_office

    @to_office.setter
    def to_office(self, to_office):
        """Sets the to_office of this GetAccountTransfersPageItems.


        :param to_office: The to_office of this GetAccountTransfersPageItems.  # noqa: E501
        :type: GetAccountTransfersPageItemsFromOffice
        """

        self._to_office = to_office

    @property
    def transfer_amount(self):
        """Gets the transfer_amount of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The transfer_amount of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: float
        """
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, transfer_amount):
        """Sets the transfer_amount of this GetAccountTransfersPageItems.


        :param transfer_amount: The transfer_amount of this GetAccountTransfersPageItems.  # noqa: E501
        :type: float
        """

        self._transfer_amount = transfer_amount

    @property
    def transfer_date(self):
        """Gets the transfer_date of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The transfer_date of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: date
        """
        return self._transfer_date

    @transfer_date.setter
    def transfer_date(self, transfer_date):
        """Sets the transfer_date of this GetAccountTransfersPageItems.


        :param transfer_date: The transfer_date of this GetAccountTransfersPageItems.  # noqa: E501
        :type: date
        """

        self._transfer_date = transfer_date

    @property
    def transfer_description(self):
        """Gets the transfer_description of this GetAccountTransfersPageItems.  # noqa: E501


        :return: The transfer_description of this GetAccountTransfersPageItems.  # noqa: E501
        :rtype: str
        """
        return self._transfer_description

    @transfer_description.setter
    def transfer_description(self, transfer_description):
        """Sets the transfer_description of this GetAccountTransfersPageItems.


        :param transfer_description: The transfer_description of this GetAccountTransfersPageItems.  # noqa: E501
        :type: str
        """

        self._transfer_description = transfer_description

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
        if issubclass(GetAccountTransfersPageItems, dict):
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
        if not isinstance(other, GetAccountTransfersPageItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
