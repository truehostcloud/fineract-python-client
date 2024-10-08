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

class GetAccountsPageItems(object):
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
        'account_no': 'int',
        'client_id': 'int',
        'client_name': 'str',
        'currency': 'GetAccountsChargesCurrency',
        'id': 'int',
        'product_id': 'int',
        'product_name': 'str',
        'purchased_shares': 'list[GetAccountsTypePurchasedShares]',
        'status': 'GetAccountsTypeStatus',
        'summary': 'GetAccountsTypeSummary',
        'timeline': 'GetAccountsTypeTimeline'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'client_id': 'clientId',
        'client_name': 'clientName',
        'currency': 'currency',
        'id': 'id',
        'product_id': 'productId',
        'product_name': 'productName',
        'purchased_shares': 'purchasedShares',
        'status': 'status',
        'summary': 'summary',
        'timeline': 'timeline'
    }

    def __init__(self, account_no=None, client_id=None, client_name=None, currency=None, id=None, product_id=None, product_name=None, purchased_shares=None, status=None, summary=None, timeline=None):  # noqa: E501
        """GetAccountsPageItems - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._client_id = None
        self._client_name = None
        self._currency = None
        self._id = None
        self._product_id = None
        self._product_name = None
        self._purchased_shares = None
        self._status = None
        self._summary = None
        self._timeline = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if currency is not None:
            self.currency = currency
        if id is not None:
            self.id = id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if purchased_shares is not None:
            self.purchased_shares = purchased_shares
        if status is not None:
            self.status = status
        if summary is not None:
            self.summary = summary
        if timeline is not None:
            self.timeline = timeline

    @property
    def account_no(self):
        """Gets the account_no of this GetAccountsPageItems.  # noqa: E501


        :return: The account_no of this GetAccountsPageItems.  # noqa: E501
        :rtype: int
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GetAccountsPageItems.


        :param account_no: The account_no of this GetAccountsPageItems.  # noqa: E501
        :type: int
        """

        self._account_no = account_no

    @property
    def client_id(self):
        """Gets the client_id of this GetAccountsPageItems.  # noqa: E501


        :return: The client_id of this GetAccountsPageItems.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetAccountsPageItems.


        :param client_id: The client_id of this GetAccountsPageItems.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this GetAccountsPageItems.  # noqa: E501


        :return: The client_name of this GetAccountsPageItems.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this GetAccountsPageItems.


        :param client_name: The client_name of this GetAccountsPageItems.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def currency(self):
        """Gets the currency of this GetAccountsPageItems.  # noqa: E501


        :return: The currency of this GetAccountsPageItems.  # noqa: E501
        :rtype: GetAccountsChargesCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetAccountsPageItems.


        :param currency: The currency of this GetAccountsPageItems.  # noqa: E501
        :type: GetAccountsChargesCurrency
        """

        self._currency = currency

    @property
    def id(self):
        """Gets the id of this GetAccountsPageItems.  # noqa: E501


        :return: The id of this GetAccountsPageItems.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAccountsPageItems.


        :param id: The id of this GetAccountsPageItems.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def product_id(self):
        """Gets the product_id of this GetAccountsPageItems.  # noqa: E501


        :return: The product_id of this GetAccountsPageItems.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this GetAccountsPageItems.


        :param product_id: The product_id of this GetAccountsPageItems.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this GetAccountsPageItems.  # noqa: E501


        :return: The product_name of this GetAccountsPageItems.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this GetAccountsPageItems.


        :param product_name: The product_name of this GetAccountsPageItems.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def purchased_shares(self):
        """Gets the purchased_shares of this GetAccountsPageItems.  # noqa: E501


        :return: The purchased_shares of this GetAccountsPageItems.  # noqa: E501
        :rtype: list[GetAccountsTypePurchasedShares]
        """
        return self._purchased_shares

    @purchased_shares.setter
    def purchased_shares(self, purchased_shares):
        """Sets the purchased_shares of this GetAccountsPageItems.


        :param purchased_shares: The purchased_shares of this GetAccountsPageItems.  # noqa: E501
        :type: list[GetAccountsTypePurchasedShares]
        """

        self._purchased_shares = purchased_shares

    @property
    def status(self):
        """Gets the status of this GetAccountsPageItems.  # noqa: E501


        :return: The status of this GetAccountsPageItems.  # noqa: E501
        :rtype: GetAccountsTypeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetAccountsPageItems.


        :param status: The status of this GetAccountsPageItems.  # noqa: E501
        :type: GetAccountsTypeStatus
        """

        self._status = status

    @property
    def summary(self):
        """Gets the summary of this GetAccountsPageItems.  # noqa: E501


        :return: The summary of this GetAccountsPageItems.  # noqa: E501
        :rtype: GetAccountsTypeSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this GetAccountsPageItems.


        :param summary: The summary of this GetAccountsPageItems.  # noqa: E501
        :type: GetAccountsTypeSummary
        """

        self._summary = summary

    @property
    def timeline(self):
        """Gets the timeline of this GetAccountsPageItems.  # noqa: E501


        :return: The timeline of this GetAccountsPageItems.  # noqa: E501
        :rtype: GetAccountsTypeTimeline
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this GetAccountsPageItems.


        :param timeline: The timeline of this GetAccountsPageItems.  # noqa: E501
        :type: GetAccountsTypeTimeline
        """

        self._timeline = timeline

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
        if issubclass(GetAccountsPageItems, dict):
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
        if not isinstance(other, GetAccountsPageItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
