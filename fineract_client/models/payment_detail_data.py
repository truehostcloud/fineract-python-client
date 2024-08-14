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

class PaymentDetailData(object):
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
        'account_number': 'str',
        'bank_number': 'str',
        'check_number': 'str',
        'id': 'int',
        'payment_type': 'PaymentType',
        'receipt_number': 'str',
        'routing_code': 'str'
    }

    attribute_map = {
        'account_number': 'accountNumber',
        'bank_number': 'bankNumber',
        'check_number': 'checkNumber',
        'id': 'id',
        'payment_type': 'paymentType',
        'receipt_number': 'receiptNumber',
        'routing_code': 'routingCode'
    }

    def __init__(self, account_number=None, bank_number=None, check_number=None, id=None, payment_type=None, receipt_number=None, routing_code=None):  # noqa: E501
        """PaymentDetailData - a model defined in Swagger"""  # noqa: E501
        self._account_number = None
        self._bank_number = None
        self._check_number = None
        self._id = None
        self._payment_type = None
        self._receipt_number = None
        self._routing_code = None
        self.discriminator = None
        if account_number is not None:
            self.account_number = account_number
        if bank_number is not None:
            self.bank_number = bank_number
        if check_number is not None:
            self.check_number = check_number
        if id is not None:
            self.id = id
        if payment_type is not None:
            self.payment_type = payment_type
        if receipt_number is not None:
            self.receipt_number = receipt_number
        if routing_code is not None:
            self.routing_code = routing_code

    @property
    def account_number(self):
        """Gets the account_number of this PaymentDetailData.  # noqa: E501


        :return: The account_number of this PaymentDetailData.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PaymentDetailData.


        :param account_number: The account_number of this PaymentDetailData.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def bank_number(self):
        """Gets the bank_number of this PaymentDetailData.  # noqa: E501


        :return: The bank_number of this PaymentDetailData.  # noqa: E501
        :rtype: str
        """
        return self._bank_number

    @bank_number.setter
    def bank_number(self, bank_number):
        """Sets the bank_number of this PaymentDetailData.


        :param bank_number: The bank_number of this PaymentDetailData.  # noqa: E501
        :type: str
        """

        self._bank_number = bank_number

    @property
    def check_number(self):
        """Gets the check_number of this PaymentDetailData.  # noqa: E501


        :return: The check_number of this PaymentDetailData.  # noqa: E501
        :rtype: str
        """
        return self._check_number

    @check_number.setter
    def check_number(self, check_number):
        """Sets the check_number of this PaymentDetailData.


        :param check_number: The check_number of this PaymentDetailData.  # noqa: E501
        :type: str
        """

        self._check_number = check_number

    @property
    def id(self):
        """Gets the id of this PaymentDetailData.  # noqa: E501


        :return: The id of this PaymentDetailData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentDetailData.


        :param id: The id of this PaymentDetailData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def payment_type(self):
        """Gets the payment_type of this PaymentDetailData.  # noqa: E501


        :return: The payment_type of this PaymentDetailData.  # noqa: E501
        :rtype: PaymentType
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this PaymentDetailData.


        :param payment_type: The payment_type of this PaymentDetailData.  # noqa: E501
        :type: PaymentType
        """

        self._payment_type = payment_type

    @property
    def receipt_number(self):
        """Gets the receipt_number of this PaymentDetailData.  # noqa: E501


        :return: The receipt_number of this PaymentDetailData.  # noqa: E501
        :rtype: str
        """
        return self._receipt_number

    @receipt_number.setter
    def receipt_number(self, receipt_number):
        """Sets the receipt_number of this PaymentDetailData.


        :param receipt_number: The receipt_number of this PaymentDetailData.  # noqa: E501
        :type: str
        """

        self._receipt_number = receipt_number

    @property
    def routing_code(self):
        """Gets the routing_code of this PaymentDetailData.  # noqa: E501


        :return: The routing_code of this PaymentDetailData.  # noqa: E501
        :rtype: str
        """
        return self._routing_code

    @routing_code.setter
    def routing_code(self, routing_code):
        """Sets the routing_code of this PaymentDetailData.


        :param routing_code: The routing_code of this PaymentDetailData.  # noqa: E501
        :type: str
        """

        self._routing_code = routing_code

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
        if issubclass(PaymentDetailData, dict):
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
        if not isinstance(other, PaymentDetailData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
