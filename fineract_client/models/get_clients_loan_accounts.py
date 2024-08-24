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

class GetClientsLoanAccounts(object):
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
        'account_no': 'str',
        'currency': 'GetClientsLoansAccountsCurrency',
        'external_id': 'str',
        'id': 'int',
        'loan_cycle': 'int',
        'loan_type': 'GetClientsLoanAccountsType',
        'product_id': 'int',
        'product_name': 'str',
        'short_product_name': 'str',
        'status': 'GetClientsLoanAccountsStatus'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'currency': 'currency',
        'external_id': 'externalId',
        'id': 'id',
        'loan_cycle': 'loanCycle',
        'loan_type': 'loanType',
        'product_id': 'productId',
        'product_name': 'productName',
        'short_product_name': 'shortProductName',
        'status': 'status'
    }

    def __init__(self, account_no=None, currency=None, external_id=None, id=None, loan_cycle=None, loan_type=None, product_id=None, product_name=None, short_product_name=None, status=None):  # noqa: E501
        """GetClientsLoanAccounts - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._currency = None
        self._external_id = None
        self._id = None
        self._loan_cycle = None
        self._loan_type = None
        self._product_id = None
        self._product_name = None
        self._short_product_name = None
        self._status = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if currency is not None:
            self.currency = currency
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if loan_cycle is not None:
            self.loan_cycle = loan_cycle
        if loan_type is not None:
            self.loan_type = loan_type
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if short_product_name is not None:
            self.short_product_name = short_product_name
        if status is not None:
            self.status = status

    @property
    def account_no(self):
        """Gets the account_no of this GetClientsLoanAccounts.  # noqa: E501


        :return: The account_no of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: str
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GetClientsLoanAccounts.


        :param account_no: The account_no of this GetClientsLoanAccounts.  # noqa: E501
        :type: str
        """

        self._account_no = account_no

    @property
    def currency(self):
        """Gets the currency of this GetClientsLoanAccounts.  # noqa: E501


        :return: The currency of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: GetClientsLoansAccountsCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetClientsLoanAccounts.


        :param currency: The currency of this GetClientsLoanAccounts.  # noqa: E501
        :type: GetClientsLoansAccountsCurrency
        """

        self._currency = currency

    @property
    def external_id(self):
        """Gets the external_id of this GetClientsLoanAccounts.  # noqa: E501


        :return: The external_id of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this GetClientsLoanAccounts.


        :param external_id: The external_id of this GetClientsLoanAccounts.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this GetClientsLoanAccounts.  # noqa: E501


        :return: The id of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetClientsLoanAccounts.


        :param id: The id of this GetClientsLoanAccounts.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def loan_cycle(self):
        """Gets the loan_cycle of this GetClientsLoanAccounts.  # noqa: E501


        :return: The loan_cycle of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: int
        """
        return self._loan_cycle

    @loan_cycle.setter
    def loan_cycle(self, loan_cycle):
        """Sets the loan_cycle of this GetClientsLoanAccounts.


        :param loan_cycle: The loan_cycle of this GetClientsLoanAccounts.  # noqa: E501
        :type: int
        """

        self._loan_cycle = loan_cycle

    @property
    def loan_type(self):
        """Gets the loan_type of this GetClientsLoanAccounts.  # noqa: E501


        :return: The loan_type of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: GetClientsLoanAccountsType
        """
        return self._loan_type

    @loan_type.setter
    def loan_type(self, loan_type):
        """Sets the loan_type of this GetClientsLoanAccounts.


        :param loan_type: The loan_type of this GetClientsLoanAccounts.  # noqa: E501
        :type: GetClientsLoanAccountsType
        """

        self._loan_type = loan_type

    @property
    def product_id(self):
        """Gets the product_id of this GetClientsLoanAccounts.  # noqa: E501


        :return: The product_id of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this GetClientsLoanAccounts.


        :param product_id: The product_id of this GetClientsLoanAccounts.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this GetClientsLoanAccounts.  # noqa: E501


        :return: The product_name of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this GetClientsLoanAccounts.


        :param product_name: The product_name of this GetClientsLoanAccounts.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def short_product_name(self):
        """Gets the short_product_name of this GetClientsLoanAccounts.  # noqa: E501


        :return: The short_product_name of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: str
        """
        return self._short_product_name

    @short_product_name.setter
    def short_product_name(self, short_product_name):
        """Sets the short_product_name of this GetClientsLoanAccounts.


        :param short_product_name: The short_product_name of this GetClientsLoanAccounts.  # noqa: E501
        :type: str
        """

        self._short_product_name = short_product_name

    @property
    def status(self):
        """Gets the status of this GetClientsLoanAccounts.  # noqa: E501


        :return: The status of this GetClientsLoanAccounts.  # noqa: E501
        :rtype: GetClientsLoanAccountsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetClientsLoanAccounts.


        :param status: The status of this GetClientsLoanAccounts.  # noqa: E501
        :type: GetClientsLoanAccountsStatus
        """

        self._status = status

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
        if issubclass(GetClientsLoanAccounts, dict):
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
        if not isinstance(other, GetClientsLoanAccounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
